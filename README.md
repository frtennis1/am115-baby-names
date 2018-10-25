Baby Name Popularity Model
==========================

About
-----

This is the repository for the work involved in Harvard's Fall 2018 Applied Math
115: Mathematical Modeling first project. It details the modeling process
alongside numerical experiments and theoretical work.

The project aims to model the evolution of baby name popularity over time in the
United States. The explicit aims are to 

1. Create a stylized model which fits baby names trends reasonably well through
   which to understand what drives baby name trends.
2. To potentially be able to use such a model for prediction of future baby name
   popularity.

Contributers
------------

- [Francisco Rivera](mailto:frivera@college.harvard.edu)
- Mark Chamberlain

Literature
----------
- Drift as a mechanism for cultural change: an example from baby names
  - <http://rspb.royalsocietypublishing.org/content/royprsb/270/Suppl_1/S120.full.pdf>
- From Karen to Katie: Using Baby Names to Understand Cultural Evolution
  - <http://journals.sagepub.com/doi/10.1177/0956797612443371>
- Analyses of baby name popularity distribution in U.S. for the last 131 years
  - <https://doi.org/10.1002/cplx.21409>
- How adoption speed affects the abandonment of cultural tastes
  - <http://www.pnas.org/content/106/20/8146>


Work Log
--------

### Wednesday Oct 24

Francisco and Mark met at office hours to settle on a topic idea. The search was
motivated by availability of data as well as transferability of models we have
seen in class. They arrived at baby names as a rich source of data for which
diffusion models could be applicable.

### Thursday Oct 25

Francisco and Mark presented the [initial slideshow](slide-show.md) of the
project. Through the Q&A, there were a couple of take-aways,

- The importance of interpretability when constructing the model.
- A potential consideration of competition among names "taking share" from each
  other.
- Simplifications when thinking about the topology of the United States
  (adjacency network, east-west dimension, north-south dimension, etc)

Data Source
-----------

The data for this project comes from <https://data.gov>. The data files are not
checked into the repository, and can be pulled from the following links.

- [National baby data](https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data)
- [State baby data](https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-data-by-state-and-district-of-)

Notebooks
---------

- [Data Exploration](01-data-exploration.ipynb) houses the initial data-reading
  code for national name data. It reads from the raw data files to create
  curated aggregations, and visualizes some of the data's trends.
