Mendeley Stats
==============

A command line tool to extract information about papers in a Mendeley folder.

## Installation

### OS X and Linux:

```
pip install numpy
pip install mendeleystats
```

Also, you need to set API keys to a configuration file. First, enter http://dev.mendeley.com/ and register an app.
to access the values of Consumer Key and Consumer Secret. With this information in hands, create a
file .mendeleystatsconfig in your home directory. The content of this file must follow the format:

```
{
    "api_key" : "the value of the consumer key",
    "api_secret" : "the value of the consumer secret"
}
```

### Windows

I do not know. I accept help to write this :)


## How to use

It is super simple to use:

```
mendeleystats [-h] --info {year,type,authors,keywords,publishedin}
                --output {chart,csv} --folder FOLDER
```

For example:

```
mendeleystats --info year --output chart --folder datamining
```

It displays a chart with information about papers per year from the "datamining" folder.
You can get other types of information, you only need to change the value of the argument --info,
the options are: year, type, authors, keywords, and publishedin.

Besides, you can choose to save a .csv file with the information instead get a chart.
For this, you need to use the value csv in the argument --output.

## Credits

I'm using two modules from https://github.com/Mendeley/mendeley-oapi-example
