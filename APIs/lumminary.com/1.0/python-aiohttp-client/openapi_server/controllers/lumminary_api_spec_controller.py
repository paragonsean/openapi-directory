from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorization import Authorization
from openapi_server.models.client_gene import ClientGene
from openapi_server.models.client_snp import ClientSNP
from openapi_server.models.javascript_web_token import JavascriptWebToken
from openapi_server.models.product import Product
from openapi_server.models.public_gene import PublicGene
from openapi_server.models.public_snp import PublicSNP
from openapi_server.models.reference_chromosome_overview import ReferenceChromosomeOverview
from openapi_server.models.reference_genome_overview import ReferenceGenomeOverview
from openapi_server.models.reference_sequence import ReferenceSequence
from openapi_server.models.report_credentials import ReportCredentials
from openapi_server.models.report_file import ReportFile
from openapi_server import util


async def get_authorizations_queue(request: web.Request, product_id, seq_num_start=None, x_fields=None) -> web.Response:
    """get_authorizations_queue

    

    :param product_id: The UUID of the product
    :type product_id: str
    :param seq_num_start: The first sequence number from which to fetch (the sequence number of the last processed authorization)
    :type seq_num_start: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_client_gene(request: web.Request, client_id, dataset_id, gene_symbol, x_fields=None) -> web.Response:
    """Get gene by symbol

    Gets A gene by its symbol, which can be found by querying the reference/ resource.  Will return a 404 if a gene exists as a reference, but its genomic coordinates intersect no SNPs in the dataset

    :param client_id: The UUID of the client
    :type client_id: str
    :param dataset_id: The UUID of one of the client&#39;s dataset
    :type dataset_id: str
    :param gene_symbol: The symbol of a gene to be fetched
    :type gene_symbol: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_client_snp(request: web.Request, client_id, dataset_id, snp_id, x_fields=None) -> web.Response:
    """Get SNP information

    Gets SNP information, as provided by the dataset.  If fetching this as an product, the client must have already granted access to the snip (see the &#39;products&#39; group)

    :param client_id: The UUID of the client
    :type client_id: str
    :param dataset_id: The UUID of one of the client&#39;s dataset
    :type dataset_id: str
    :param snp_id: The rsId of a SNP to be fetched
    :type snp_id: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_client_snp_group(request: web.Request, client_id, dataset_id, x_fields=None) -> web.Response:
    """get_client_snp_group

    

    :param client_id: The UUID of the client
    :type client_id: str
    :param dataset_id: The UUID of one of the client&#39;s dataset
    :type dataset_id: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_gene(request: web.Request, database_name, accession, dbsnp_build=None, reference_genome=None, x_fields=None) -> web.Response:
    """Generic gene information

    

    :param database_name: The name of the database to search. E.g: Genbank
    :type database_name: str
    :param accession: The accession within the selected database
    :type accession: str
    :param dbsnp_build: The dbSNP build for which to consider snps belonging to the gene. Defaults to 149
    :type dbsnp_build: int
    :param reference_genome: The reference genome for which gene annotations will be returned. Defaults to GRCh37p13
    :type reference_genome: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_product(request: web.Request, product_id, x_fields=None) -> web.Response:
    """Get product details

    

    :param product_id: The UUID of the product
    :type product_id: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_product_authorization(request: web.Request, product_id, authorization_id, x_fields=None) -> web.Response:
    """get_product_authorization

    

    :param product_id: The UUID of the product
    :type product_id: str
    :param authorization_id: The UUID of the authorization
    :type authorization_id: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_reference_chromosome(request: web.Request, genome_build_accession, chromosome_accession, range_start, range_stop, x_fields=None) -> web.Response:
    """Sequence for a region of the reference genome

    Fetch a closed interval of nucleotides on a given chromosome. Includes start and stop positions

    :param genome_build_accession: The accession of the reference genome
    :type genome_build_accession: str
    :param chromosome_accession: The accession to the chromosome
    :type chromosome_accession: str
    :param range_start: Location on the chromosome
    :type range_start: int
    :param range_stop: Location on the chromosome
    :type range_stop: int
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_reference_genome(request: web.Request, genome_build_accession, x_fields=None) -> web.Response:
    """Reference genome metadata

    

    :param genome_build_accession: 
    :type genome_build_accession: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_reference_genomes_group(request: web.Request, x_fields=None) -> web.Response:
    """Reference genome builds

    Lists reference genome builds that are available

    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def get_reference_snp(request: web.Request, snp_accession, dbsnp_version=None, grch_version=None, x_fields=None) -> web.Response:
    """Reference SNP data

    Get reference SNP information, from dbSNP

    :param snp_accession: The rsId of the SNP
    :type snp_accession: str
    :param dbsnp_version: The dbSNP build. Defaults to 149
    :type dbsnp_version: int
    :param grch_version: The GRCh build on which to place snips. Defaults to GRCh37p13
    :type grch_version: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def post_authorization_result_credentials(request: web.Request, product_id, authorization_id, x_fields=None, credentials_username=None, credentials_password=None, report_url=None) -> web.Response:
    """Provide a result for the authorization

    These can be log-in credentials for a website where the result is available

    :param product_id: The UUID of the product
    :type product_id: str
    :param authorization_id: The UUID of the authorization
    :type authorization_id: str
    :param x_fields: An optional fields mask
    :type x_fields: str
    :param credentials_username: Credentials for accessing the result. Includes password, username and url
    :type credentials_username: str
    :param credentials_password: Credentials for accessing the result. Includes password, username and url
    :type credentials_password: str
    :param report_url: Credentials for accessing the result. Includes password, username and url
    :type report_url: str

    """
    return web.Response(status=200)


async def post_authorization_result_file(request: web.Request, product_id, authorization_id, original_filename=None, x_fields=None, file_report=None) -> web.Response:
    """Provide a file result to the authorization, e

    g. a pdf report

    :param product_id: The UUID of the product
    :type product_id: str
    :param authorization_id: The UUID of the authorization
    :type authorization_id: str
    :param original_filename: Optional original filename for the report. If not provided, the filename of uploaded file will be used
    :type original_filename: str
    :param x_fields: An optional fields mask
    :type x_fields: str
    :param file_report: A binary file (e.g. pdf) that contains the result of the authorization
    :type file_report: str

    """
    return web.Response(status=200)


async def post_client_snp_group(request: web.Request, client_id, dataset_id, snps, x_fields=None) -> web.Response:
    """Get a large group of SNPs

    SNPs that are not present in the dataset are ignored, 404 is returned only if the dataset/client does not exist

    :param client_id: The UUID of the client
    :type client_id: str
    :param dataset_id: The UUID of one of the client&#39;s dataset
    :type dataset_id: str
    :param snps: JSON-encoded list of snps to be fetched
    :type snps: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def post_jwt_auth(request: web.Request, username, password, role, x_fields=None) -> web.Response:
    """General-purpose authentication

    ## Note: * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format &#x60;Bearer: your-token-here&#x60; * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued

    :param username: The email for a Client, or the API for a partner product
    :type username: str
    :param password: The passowrd for a Client, or the API key for a service
    :type password: str
    :param role: The role for which authentication will be made. Value : role_product
    :type role: str
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)


async def post_product_authorization(request: web.Request, product_id, authorization_id) -> web.Response:
    """Signal that processing is complete, without uploading any result

    

    :param product_id: The UUID of the product
    :type product_id: str
    :param authorization_id: The UUID of the authorization
    :type authorization_id: str

    """
    return web.Response(status=200)


async def post_product_authorization_unfulfillable(request: web.Request, product_id, authorization_id) -> web.Response:
    """Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons

    

    :param product_id: The UUID of the product
    :type product_id: str
    :param authorization_id: The UUID of the authorization
    :type authorization_id: str

    """
    return web.Response(status=200)
