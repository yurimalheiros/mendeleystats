import csv
import itertools
from pylab import *
import numpy.numarray as na
from mendeleystats.mendeley_client import *
from collections import Counter

class Folder(object):
    def __init__(self, config_file):
        self.folder_id = None
        self.documents = []
        self.years_counter = None
        self.types_counter = None
        self.keywords_counter = None
        self.authors_counter = None
        self.published_in_counter = None

        self.mendeley = create_client(config_file)

    ########## Public methods. ##########

    def load_data(self, folder_name):
        """
        Load folder data from the Mendeley server.

        Args:
            folder_name: the name of the folder.
        """
        folders = self.mendeley.folders()

        for folder in folders:
            if folder["name"] == folder_name:
                self.load_data_by_id(folder["id"])

    def load_data_by_id(self, folder_id):
        """
        Load folder data from the Mendeley server.

        Args:
            folder_id: the id of the folder.
        """
        documents_request = self.mendeley.folder_documents(folder_id, items=999)
        documents = documents_request["documents"]
        self.documents = [self.mendeley.document_details(d["id"]) for d in documents]

        self.years_counter = self._get_years_counter()
        self.types_counter = self._get_types_counter()
        self.keywords_counter = self._get_keywords_counter()
        self.authors_counter = self._get_authors_counter()
        self.published_in_counter = self._get_published_in_counter()

    def plot_years(self):
        """Show a chart with papers per year."""
        self._plot(self.years_counter)

    def plot_types(self):
        """Show a chart with papers per publication type."""
        self._plot(self.types_counter)

    def plot_keywords(self):
        """Show a chart with papers per keyword."""
        self._plot(self.keywords_counter)

    def plot_authors(self):
        """Show a chart with papers per author."""
        self._plot(self.authors_counter)

    def plot_published_in(self):
        """Show a chart with papers per published outlet."""
        self._plot(self.published_in_counter)

    def csv_years(self):
        """Create a .csv file with papers per year data."""
        self._save_csv(self.years_counter, "years.csv")

    def csv_types(self):
        """Create a .csv file with papers per publication type data."""
        self._save_csv(self.types_counter, "types.csv")

    def csv_keywords(self):
        """Create a .csv file with papers per keyword data."""
        self._save_csv(self.keywords_counter, "keywords.csv")

    def csv_authors(self):
        """Create a .csv file with papers per author data."""
        self._save_csv(self.authors_counter, "authors.csv")

    def csv_published_in(self):
        """Create a .csv file with papers per published outlet data."""
        self._save_csv(self.published_in_counter, "published.csv")


    ########## Private methods. ##########

    def _get_years_counter(self):
        """Return a Counter of papers per year."""
        year = []
        for d in self.documents:
            year.append(d.get("year", "not defined")) 

        return Counter(year)

    def _get_types_counter(self):
        """Return a Counter of papers per publication type."""
        type = []
        for d in self.documents:
            type.append(d.get("type", "not defined")) 

        return Counter(type)

    def _get_keywords_counter(self):
        """Return a Counter of papers per keyword."""
        keywords = [d["keywords"] for d in self.documents]
        keywords = list(itertools.chain.from_iterable(keywords))

        keywords_aux = []
        for k in keywords:
            keywords_aux.extend(k.split(";"))

        keywords = keywords_aux
        keywords = [k.strip() for k in keywords]
        keywords = filter(lambda x: x!="", keywords)

        return Counter(keywords)

    def _get_authors_counter(self):
        """Return a Counter of papers per author."""
        authors = [d["authors"] for d in self.documents]
        authors_fullname = []
        for author_list in authors:
            for author in author_list:
                authors_fullname.append(author["forename"] + " " + author["surname"])

        return Counter(authors_fullname)

    def _get_published_in_counter(self):
        """Return a Counter of papers per publish outlet."""
        published = []
        for d in self.documents:
            published.append(d.get("published_in", "not defined")) 

        return Counter(published)
        
        
    def _plot(self, counter, vertical=False):
        """Create a chart with a Counter data."""
        labels = counter.keys()
        labels.sort()
        data = [counter[l] for l in labels]
        
        xlocations = na.array(range(len(data)))+0.5
        width = 0.5

        bar(xlocations, data, width=width)
        tlocs, tlabels = xticks(xlocations+width/2, labels)
        xlim(0, xlocations[-1]+width*2)
        title("Papers")
        gca().get_xaxis().tick_bottom()
        gca().get_yaxis().tick_left()
        
        if vertical:
            setp(tlabels, "rotation", "vertical")

        show()

    def _save_csv(self, counter, filename):
        """Create a .csv file with a Counter data."""
        with open(filename, 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            writer.writerows(counter.items())




