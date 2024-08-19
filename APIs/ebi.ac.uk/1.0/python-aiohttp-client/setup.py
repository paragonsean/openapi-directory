# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="CROssBAR Data API",
    author_email="crossbar_dev@ebi.ac.uk",
    url="",
    keywords=["OpenAPI", "CROssBAR Data API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # About CROssBAR &amp; data **CROssBAR**: Comprehensive Resource of Biomedical Relations with Deep Learning Applications and Knowledge Graph Representations CROssBAR is a comprehensive system that integrates large-scale biomedical data from various resources e.g UniProt, ChEMBL, Drugbank, EFO, HPO, InterPro &amp; PubChem and stores them in a new NoSQL database, enrich these data with deep learning based prediction of relations between numerous biomedical entities, rigorously analyse the enriched data to obtain biologically meaningful modules and display them to the user via easy to interpret, interactive and heterogeneous knowledge graphs. CROssBAR platform exposes a set of 12 endpoints to query data stored in the CROssBAR database. These endpoints help the user to find data of interest using different parameters provided by the API endpoint. For example, https://www.ebi.ac.uk/tools/crossbar/proteins?accession&#x3D;A0A023GRW5 -&gt; will provide protein information about accession &#39;A0A023GRW5&#39; including its interactions, functions, cross-references, variations and more. https://www.ebi.ac.uk/tools/crossbar/activities?moleculeChemblId&#x3D;CHEMBL465983 -&gt; will provide ChEMBL bio-interactions related information including targets and bio-activity measurements associated with molecule chembl id &#39;CHEMBL465983&#39;  **Knowledge graphs** Another use case of CROssBAR&#39;s API endpoints is in building knowledge graphs. These endpoints can be *weaved* together (output from one API endpoint fed as input to another API endpoint) programmatically to link nodes like protein, disease, drugs etc. as nodes of the graph. The endpoints are designed to be independent from each other which allows users the flexibility to drive biological networks from any facet e.g drug-centric, disease-centric, gene-centric etc. Our service for knowledge graph construction is available at https://crossbar.kansil.org. An example for the part of the background queries on the CROssBAR API during the construction of a knowledge graph,  (with the aim of keeping the example simple, we have only included the processes related to pathways, genes/proteins and drugs/compounds) In this example, we would like to find bio-active compounds (with a pChEMBL value threshold of at least 6.0) &amp; drugs targeting all proteins belonging to \&quot;WNT ligand biogenesis and trafficking\&quot; pathway (based on Reactome pathway annotations). This can be achieved by using endpoints listed on this swagger documentation as illustrated in following steps- Find bio-active compounds (with a pChEMBL value threshold of at least 6.0) &amp; drugs targeting all proteins belonging to \&quot;WNT ligand biogenesis and trafficking\&quot; pathway (based on Reactome annotations) This can be achieved by using endpoints listed on [this swagger documentation](https://www.ebi.ac.uk/tools/crossbar/swagger-ui.html) as illustrated in following steps- 1. Get all proteins from “/proteins” API endpoint which have a reactome pathway name equal to \&quot;WNT ligand biogenesis and trafficking\&quot;. 2. From the collection of uniprot protein accessions collected from step 1 above, we query “/targets” API endpoint to obtain the ‘target_chembl_id’s of these proteins. 3. From the collection of target_chembl_ids collected from step 2 above, we query “/activities” API endpoint with pChEMBL value &gt;&#x3D;6, to obtain the ’molecule_chembl_id’s of the molecules that we need.  4. From the collection of uniprot protein accessions collected from step 1 above, we find out Drug names and ids from the “/drugs” API endpoint that targets our proteins. 5. From the collection of ’molecule_chembl_id’s obtained in step3, we query “/molecules” endpoint to get the compounds that are interacting with the genes/proteins belonging to the “WNT ligand biogenesis and trafficking” pathway.
    """
)

