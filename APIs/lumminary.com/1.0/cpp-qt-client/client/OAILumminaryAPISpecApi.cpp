/**
 * Lumminary API
 * # Introduction The Lumminary API was built to allow third parties to interact with Lumminary customers and gain access to their genetic data. The Lumminary API is fast, scalable and highly secure. All requests to the Lumminary API take place over SSL, which means all communication of Customer data is encrypted.  Before we dive in, some definitions. This is what we mean by:  |Term|Definition| |-----------|-----------| |**Third party**|A third party (also referred to as \"partner\" or as \"you\") is a company which offers services and products using genetic data.| |**Lumminary clients**|The Lumminary client (also referred to as \"customer\") is an individual who has created an account on the Lumminary platform.| |**Lumminary**|This is  us - our services including the Lumminary platform, the API, the DNA App Store, the DNA Vault, the \"Connect with Lumminary\" button, and the website in its totality. | |**CWL**|This is the acronym for the \"Connect with Lumminary\" button.| |**dataset**|This is the term we use when we refer to a customer's genetic data.| |**Lumminary API**|This is a library/module that you can use to integrate your apps with the Lumminary platform.| |**Lumminary toolkit**|This is a stand alone application which helps you integrate with Lumminary without writing any code or interacting with the Lumminary API.|  Let's dive in, now.  * [**Overview**](#section/Introduction/Overview)  * [**Install Lumminary API Client and Toolkit**](#Install-Lumminary-API-Client-andor-Toolkit) * [**Obtaining credentials**](#Obtaining-credentials) * [**Query customers authorizations**](#Query-customers-authorizations) * [**Query customer genetic data**](#Query-customer-genetic-data) * [**Submit reports**](#Submit-reports)  * [**\"Connect with Lumminary\" button**](#the-connect-with-lumminary-button)  * [**API specs**](#tag/Lumminary)  ## Overview  In order to use Lumminary services, you'll need to install the Lumminary API Client or Toolkit. The Lumminary API Client and Toolkit are available in multiple programming languages, and we also provide a sandbox environment which you can use for integration and tests.  There are a couple of differences between the API Client and the Toolkit. Mainly, it's about the ease of use for integration. The Toolkit is basically a stand-alone application that facilitates the integration with the Lumminary API without the need to modify your already existing code.  You use the Lumminary API Client when you want to integrate it inside your own application. This means it gives you full flexibility regarding the integration into your own workflow.  You use the Lumminary Toolkit for an integration where the Toolkit is placed alongside your own application. You can use the Toolkit from the CLI - for example, to run a cronjob that processes incoming orders. The Toolkit uses the Lumminary API Client.  # Install Lumminary API Client and/or Toolkit  We provide the Lumminary API Client and Toolkit in multiple programming languages - default are PHP (minimum version 7.0), Python2.7 and Python3. However, if you need them in another language (Java, Obj-C, JavaScript, C#, Perl, CURL), please contact us.   ## How to install the Lumminary API Client  #### PHP example: The PHP Lumminary API Client is available at: https://github.com/Lumminary/lumminary-api-client-php  If you are already using [Composer](https://getcomposer.org), you can import the project by adding the following to your `composer.json` ```json \"repositories\": [     {         \"type\": \"git\",         \"url\": \"https://github.com/Lumminary/lumminary-api-client-php.git\",         \"reference\": \"master\"     } ], \"require\": {     \"lumminary/api-client-php\": \"v1.0.6\" } ```  Then run `composer update lumminary/api-client-php`  #### Python example:  The Python Lumminary API Client is available at: https://github.com/Lumminary/lumminary-api-client-python  To install directly, run  ```bash pip install git+https://git@github.com/Lumminary/lumminary-api-client-python.git@v1.0.7#egg=lumminary-api-client ```  Or add the following line in your requirements.txt  ```bash git+https://git@github.com/Lumminary/lumminary-api-client-python.git@v1.0.7#egg=lumminary-api-client ```  ## How to install the Lumminary Toolkit  #### PHP example: The PHP Lumminary Toolkit is available at: https://github.com/Lumminary/lumminary-toolkit-php  To install the Lumminary Toolkit, run the following command where 'lumminary-toolkit-directory' is the directory where you want to install the Lumminary Toolkit:  `git clone git@github.com:Lumminary/lumminary-toolkit-php.git lumminary-toolkit-directory`  #### PYTHON example:  The Python Lumminary Toolkit is available at: https://github.com/Lumminary/lumminary-toolkit-python  To install the Lumminary Toolkit, run the following command where 'lumminary-toolkit-directory' is the directory where you want to install the Lumminary Toolkit:  ```bash git clone git@github.com:Lumminary/lumminary-toolkit-python.git lumminary-toolkit-directory cd lumminary-toolkit-directory virtualenv env source env/bin/activate pip install -r requirements.txt ```  Note that before running the toolkit, you should have the virtualenv enabled, like so : `source lumminary-toolkit-directory/env/bin/activate`  ## Toolkit Setup  We recommend to run the Toolkit in a cronjob; at every run it will check for new Authorizations (Orders) and will download them; afterwards it will check for a new reports folder inside the old authorizations, process the reports, and delete the processed Authorizations and Reports from your server.   The first step after you clone the Lumminary Toolkit project for your language is to configure it with your credentials.   Go to the Lumminary Toolkit base diretory `cd lumminary-toolkit-directory`. Under the Toolkit directory, you will find a file `config/config_template.json` which has the following structure:  ```json {     \"api_key\": <your-api-key>,     \"product_uuid\": <your-product-uuid>,     \"api_host\": \"https://api.lumminary.com/v1\",     \"output_root\": <your-authorization-data-basepath>,     \"export_handler\": <your-export-handler-class>,     \"product_name\": <your-product-name>,     \"operations\": [         \"pull_datasets\",         \"push_reports\"     ],     \"optional\": {         \"dna_data_filename\": \"dna-data.tsv\",         \"authorization_metadata_filename\": \"authorization-metadata.json\"     } } ```  You should copy this config `cp config/config_template.json config/my-product1-config.json` then edit it `vim config/my-product1-config.json` to contain the following values:  | Config attribute | Example Value                      | Description | |------------------|------------------------------------|-------------| | api_key        | `\"TiiU...bqg==\"`                   |Your Lumminary API key.<br> You can obtain it from the Lumminary Admin  | | product_uuid   | `\"1234-1234-1234-1234\"`            |Your product UUID. This value can be obtained from the Lumminary Admin | | api_host       | `\"https://api.lumminary.com/v1\"`   |   The API endpoint to use.<br>For the sandbox environment you can use \"https://sandbox-api.lumminary.com/v1\"    | | output_root    | `\"/var/lumminary-orders/product1/\"`         | The base directory where the Toolkit places the Authorizations for your Product <br> The Lumminary Toolkit will *never* overwrite Authorization data or create this directory, to protect from overwrites or typos    | | export_handler |`\"export_handler_tsv\"`  | If you have a custom export handler, then your Lumminary contact will provide you with the name of your export handler.   | | operations       |`[\"pull_datasets\", \"push_reports\"]`        | These are two optional parameters that define the tasks that the Toolkit should perform. Possible values are: <br> 1. `pull_datasets` - this tells the Toolkit to download the Customer Authorization (Customer details and genetic data) <br> 2. `push_reports` - this tells the Toolkit to push the results to the API; see below for more details| | optional       | `{}`                               | Export handler specific value |  After updating the config file for your Toolkit, it should look similar to (Note that these are all dummy values) :  ```json {     \"api_key\": \"TiiU...bqg==\",     \"product_uuid\": \"1234-1234-1234-1234\",     \"api_host\": \"https://api.lumminary.com/v1\",     \"output_root\": \"/var/lumminary-orders/product1/\",     \"export_handler\": \"export_handler_tsv\",     \"product_name\": \"product 1\",     \"operations\": [         \"pull_datasets\",         \"push_reports\"     ],     \"optional\": {         \"dna_data_filename\": \"dna-data.tsv\",         \"authorization_metadata_filename\": \"authorization-metadata.json\"     } } ```  You can now save and exit the text editor `:wq` and start polling the API for new Authorizations :  Python  ```bash # While still in the <lumminary-toolkit> directory source env/bin/activate; python lumminary_partner_toolkit.py --config-path config/my-lumminary-product1-config.json ```  PHP  ```bash # While still in the <lumminary-toolkit> directory php lumminary-partner-toolkit.php --config-path config/my-lumminary-product1-config.json ```  When your Product receives new Authorizations, the Toolkit will pull all the relevant data and save it in the following files:  ```bash # The DNA data file. Format compatible with 23AndMe by default <output_root>/<authorization_uuid>/dna-data.tsv  # The Authorization metadata <output_root>/<authorization_uuid>/authorization.json ```  The contents of the files pulled when processing an Authorization are as follows:  ```bash $ head -n 5 <output_root>/<authorization_uuid>/dna-data.tsv # rsid      chromosome  position        genotype rs12070387  1           6267531         CC rs149124387 1           12025561        CC rs116458387 1           14920119        AA rs4436387   1           15498452        CC  $ cat <output_root>/<authorization_uuid>/authorization.json  {     \"authorization\": <authorization_uuid>,     \"created_timestamp_utc\": 1542920184,     \"customer\": <customer_uuid>,     \"customer_address\": {         \"address1\": <address1>,         \"address2\": <address2>,         \"city\": <city>,         \"country\": <country>,         \"state\": <state>,         \"zipcode\": <zipcode>      },     \"customer_email\": <customer_email>,     \"customer_name\": {         \"first_name\": <customer_first_name>,         \"last_name\": <customer_last_name>     },     \"dataset\": <dataset_uuid>,     \"product\": <your_product_uuid> } ```  After the Toolkit downloaded the Authorizations, you need to process the Customer genetic data file and the Customer details, individually. The Lumminary API supports multiple types of products:  | Scenario | How to Report |                     |------------------|------------------------------------| |The product is a file (.pdf, .jpeg etc.) | Put the result file(s) into the `tmp_reports` directory. Please refer to the Note underneath this table. | |The product requires authentication | Create a file with the name `result.json` into the `tmp_reports` directory, with the following content: <br> `{ \"credentials\": { \"username\": \"username@example.com\", \"password\": \"your generated password\", \"url\": \"https://your-website.com/report\"}}`<br> The `url` should point to a login page that upon authentication redirects the user to the report page. You can find the customer's email address in the `authorization-metadata.json` and the `password` attribute must be a secure password. Please refer to the Note underneath this table. | |The product is a physical product| Create a file with the name `result.json` into the `tmp_reports` directory, with the following content: <br> `{\"physical_product\": { \"physical_product_completed\": true }}` <br> This should be done upon dispatch. Please refer to the Note underneath this table. | |An error occurred| Create a file with the name `result.json` into the `tmp_reports` directory, with the following content: <br> `{ \"unfulfillable\": {\"error\": \"Reasons for why it is unfulfillable\", }}` <br> The error message is for Lumminary internal usage, and it won't be visible to the customer. This will delete your Authorization, making it unuseable thereafter. So please use this only for unfixable errors, and never for temporary errors you attempt to resolve. Please refer to the Note underneath this table. |  ###### Note For each scenario above, we recommend you use a temporary directory to avoid uploading incomplete files or reports. So your workflow should be: * create a temporary directory inside the `<output_root>/<authorization_uuid>`, such as `<output_root>/<authorization_uuid>/tmp_reports/`   * place your result file(s) in the `tmp_reports` directory (as in the above table) * rename the directory from `tmp_reports` to `reports`  We recommend running the Toolkit in a cronjob, wrapped by some locking mechanism. Also, Toolkit logs are very minimal but can be very helpful when debugging an issue, so please consider saving them to a file. For example, the following cronjob runs the Toolkit every minute:  ```bash # Open the crontab crontab -e ```  PHP Toolkit  ```bash # Add the following line (replace <lumminary-toolkit-directory> with the absolute path of the Lumminary Toolkit) * * * * * flock /var/lock/lumminary-toolkit.lock php <lumminary-toolkit-directory>/lumminary-partner-toolkit.php --config-path <lumminary-toolkit-directory>/config/my-product1-config.json >> /var/log/lumminary-toolkit.log ```  Python Toolkit  ```bash # Add the following line (replace <lumminary-toolkit-directory> with the absolute path of the Lumminary Toolkit) * * * * * flock /var/lock/lumminary-toolkit.lock source env/bin/activate; python <lumminary-toolkit-directory>/lumminary_partner_toolkit.py --config-path <lumminary-toolkit-directory>/config/my-product1-config.json ```  ## API endpoints Lumminary provides two endpoint APIs, sandbox and production. You can use the sandbox for your integration and testing, simulate orders, upload genetic data, and generate reports. The sandbox works exactly like the production environment, and you can test your end-to-end integration.  In order to simulate a complete order, you need to use this test credit card:   |Credit card number  | Expiration date| CVV2| |--------------------|----------------|-----| |4242 4242 4242 4242 |  12/30         | 123 |  ### Sandbox website: [sandbox-www.lumminary.com](https://sandbox-www.lumminary.com)  api-hostname: [sandbox-api.lumminary.com/v1](https://sandbox-api.lumminary.com/v1)  ### Production website: [lumminary.com](https://lummianary.com)  api-hostname: [api.lumminary.com/v1](https://api.lumminary.com/v1)  # Obtaining credentials To obtain credentials, you need to register as a Lumminary partner. You can do this by [filling in this form](https://lumminary.com/register-for-connect-with-lumminary).  You will then receive the following:  |Credentials|Description| |-------|-------| |Product UUID|Each product you register on the Lumminary platform gets an UUID which will be used to identify that product to the Lumminary API| |API key|The secret API key associated with the Product UUID| |Partner UUID|Upon your first registration on the Lumminary platform, you will receive a single Partner UUID, which identifies you as one entity, regardless of product. This identifier is used for the Connect with Lumminary (CWL) functionality.| |CWL Encryption Key|The CWL encryption key is associated with the Partner UUID and is used to encrypt all communication for the Connect with Lumminary functionality.|  Each product or service needs to have its own product UUID and API key, which means you have to fill in the form for all products and services that require access to Lumminary customer data.    ## Configure the credentials to the Lumminary API Client The easiest way to set up your credentials is to use an environment file.  For this, you must create a file named `env.json` (but any name will do) in your project directory, which should contain: ```json {     \"product_uuid\": <your_product_uuid>,     \"api_key\": <your_product_api_key>,     \"role\": \"role_product\",     \"api_host\": <lumminary_api_hostname_endpoint> } ```  In order to load the Credentials from the `env.json`, you can use the following code:  #### PHP example: ```php require_once(__DIR__.\"/vendor/autoload.php\"); $credentials = new Lumminary\\Client\\Credentials(); $credentials->loadJSONCredentials(__DIR__.\"/env.json\"); ```  #### Python example: ```python import lumminary_sdk as lumminary import os  credentials = lumminary.Credentials() credentials.load_json_credentials(     os.path.join(         os.getcwd(),         \"env.json\"     ) ) ```  ## Alternative credentials configuration You also have the option of passing the credentials as constructor parameters when instantiating the `Credentials` class.  #### PHP example:  ```php require_once(__DIR__.\"/vendor/autoload.php\"); $credentials = new Lumminary\\Client\\Credentials(     <lumminary_api_hostname_endpoint>,     <your_product_uuid>,     <your_product_api_key> ); ```  #### Python example:  ```python import lumminary_sdk as lumminary  credentials = lumminary.Credentials(     product_uuid = <your_product_uuid>,     api_key = <your_product_api_key>,     api_host = <lumminary_api_hostname_endpoint>,     role = \"role_product\" ) ```  ## Create an API instance  With the credentials configured and loaded, you can create an API client like so :   #### PHP example  ```php $apiClient = new Lumminary\\Client\\ApiClient($credentials); ```  #### Python example  ```python apiClient = lumminary.LumminaryApi(credentials) ```  # Query customers authorizations An Authorization represents permission from a client to access their personal and genetic data.   There are 2 situations where customers grant you access to their data:  * when a customer buys your product from the Lumminary DNA App Store * when a customer clicks on the \"Connect with Lumminary\" button on your website  Each time either of the above situations happens, our platform creates an Authorization UUID. You can reliably assume that if you have an Authorization UUID, you automatically have access to all the personal information and genetic data needed by your products and services. After you process an Authorization you need to mark it as processed; processed Authorizations will no longer be on the list of new authorizations.  There are two ways to obtain the Authorization UUID: * _polling_ - this method allows you to periodically interrogate our API and pulls the list of Authorization UUIDs.  * _webhooks_ (coming soon) - this method allows our API to push the Authorization UUIDs into your platform.  ## Poll method  To use the polling method, your servers periodically interrogate for new Authorization UUIDs. Please keep in mind that Authorizations not marked as processed will always be returned when polling for new Authorizations. This means there's a risk of parallel processing the same Authorization. To avoid this, you can, for example, consider using locking when processing.  #### A PHP example of using the polling API looks like:  ```php $productAuthorizations = $apiClient->getAuthorizationsQueue(     $apiClient->getCredentials()->getProductUuid(), );  foreach($productAuthorizations as $productAuthorization) {     /_**      *  Add your code for processing customer data here      **_/           // Mark Authorization as processed      $apiClient->postProductAuthorization(         $productAuthorization[\"productUuid\"],         $productAuthorization[\"authorizationUuid\"]     ); } ```  #### A Python example of using the polling API looks like:  ```python productAuthorizations = apiClient.get_authorizations_queue(     apiClient.get_credentials().product_uuid )  for productAuthorization in productAuthorizations:     #######     #   Add your code for processing customer data here     #######      # Mark Authorization as processed     apiClient.post_product_authorization(         productAuthorization.product_uuid,         productAuthorization.authorization_uuid     ) ```  Based on the Authorization object obtained previously, we can now query the customer's information (personal details and genetic data).  #### PHP example: ```php $authorizationMetadata = $apiClient->authorizationMetadata($productAuthorization[\"authorizationUuid\"]); ```  #### Python example: ```python authorizationMetadata = apiClient.authorization_metadata(productAuthorization.authorization_uuid) ```  #### authorizationMetadata object object structure  | Attribute name            | Description                                                                                | |:-------------------------:|:-------------------------------------------------------------------------------------------| | `customer`                | The UUID of the customer granting the Authorization                                        | | `product`                 | The UUID of the product that was authorized (your product UUID)                            | | `authorization`           | The UUID of the granted Authorization.                                                     | | `created_timestamp_utc`   | The unix timestamp in UTC time zone when the customer granted the Authorization            | | `dataset`                 | (present only if requested) The UUID of the dataset authorized by the customer             | | `customer_email`          | (present only if requested) Customer contact email                                         | | `customer_name`           | (present only if requested) Customer name                                                  | | `customer_address`        | (present only if requested) Customer address                                               |  By *present only if requested* we mean this attribute will be returned if at the time of configuring either the \"Connect with Lumminary\" button or your product, you have explicitly requested for that particular set of data.  # Query customer genetic data Based on the Authorization object obtained previously, now we have authorizationMetadata which contains the customer's information (personal details and genetic data). Let's use this information to extract some customer genetic data.  ## Get individual SNPs Out of all the available SNPs in the dataset, you can only access those for which the customer has previously granted permission.  For example, fetching details for a particular SNP:  #### PHP example: ```php $rsId = \"rs114326054\"; $snpDetails = null;  // check to see if you have access to the customer genetic data if (isset($productAuthorization[\"scopes\"][\"dataset\"])) {     // get SNP information     $snpDetails = $apiClient->getClientSnp(         $productAuthorization[\"clientUuid\"],         $productAuthorization[\"scopes\"][\"dataset\"],         $rsId     ); } ```  #### Python example: ```python rsId = \"rs114326054\" snpDetails = None  # check to see if you have access to the customer genetic data if hasattr(productAuthorization.scopes, \"dataset\"):     # get SNP information     snpDetails = apiClient.get_client_snp(         productAuthorization.client_uuid,         productAuthorization.scopes.dataset,         rsId     ) ```  ##### The snpDetails object will contain these important attributes:  | Attribute name PHP     | Attribute name Python        | Description                                               | |:-------------------------:|:-------------------------:|:----------------------------------------------------------| | `snpId`                 | `snp_id`                    | The rsid of the SNP                                       | | `referenceGenome`        |`reference_genome`          | The reference genome known to be used by the Dataset's source. <br> This impacts the reference allele, location, and based on the dbSNP build, also the SNP's accession | | `genotypedAlleles`       | `genotyped_alleles`        | The genotype value of the customer's queried SNP. <br><br> If the attribute of this SNP has the `phased` flag set to True, <br>the first items in the lists for all SNPs will be on the same inherited chromosome, <br>and analogous for the second item. <br><br> If the SNP is unphased, the order of the items is irrelevant | |`phased`                   | `phased`                  | A boolean. True if the SNP is known to be phased, False otherwise | |`chromosomeAccession`     | `chromosome_accession`     | This is the chromosome accession number where the SNP is located; in the format of NC_00x | |`location`                 | `location`                | This is the customer's SNP's location on the chromosome |  When trying to access any customer's SNP for which you don't have permission, an `Unauthorized` exception will be raised.  ## Get all authorized SNPs  The function below returns all SNPs your product has access to. These are all the SNPs configured as mandatory for your product, as well as all SNPs that are configured as optional and available in the customer's data set. We encourage you to use this option if you need to get all available SNPs, because it is faster than fetching SNP details one by one.  For example, fetching all authorized SNPs:  #### PHP example: ```php $datasetSnps = null;  // check to see if you have access to the customer genetic data if (isset($productAuthorization[\"scopes\"][\"dataset\"])) {     // get all authorized SNPs     $datasetSnps = $apiClient->getClientSnpGroup(         $productAuthorization[\"clientUuid\"],          $productAuthorization[\"scopes\"][\"dataset\"]     ); } ```  #### Python example: ```python datasetSnps = None  # check to see if you have access to the customer genetic data if hasattr(productAuthorization.scopes, \"dataset\"):     # get all authorized SNPs     datasetSnps = apiClient.get_client_snp_group(         productAuthorization.client_uuid,         productAuthorization.scopes.dataset     ) ```  ##### The datasetSnps variable will be a list of objects each having the following attributes:  | Attribute name PHP     | Attribute name Python        | Description                                               | |:-------------------------:|:-------------------------:|:----------------------------------------------------------| | `snpId`                  | `snp_id`                   | The rsid of the SNP                                       | | `referenceGenome`        |`reference_genome`          | The reference genome known to be used by the Dataset's source. <br> This impacts the reference allele, location, and based on the dbSNP build, also the SNP's accession | | `genotypedAlleles`       | `genotyped_alleles`        | The genotype value of the customer's queried SNP. <br><br> If the attribute of this SNP has the `phased` flag set to True, <br>the first items in the lists for all SNPs will be on the same inherited chromosome, <br>and analogous for the second item. <br><br> If the SNP is unphased, the order of the items is irrelevant | |`phased`                   | `phased`                  | A boolean. True if the SNP is known to be phased, False otherwise | |`chromosomeAccession`     | `chromosome_accession`     | This is the chromosome accession number where the SNP is located; in the format of NC_00x | |`location`                 | `location`                | This is the customer's SNP's location on the chromosome |  When trying to access any customer's SNP for which you don't have permission, an `Unauthorized` exception will be raised.  ## Get Genes  Along with individual SNPs, you can also get all the authorized SNPs from a particular gene, that are available in the customer's dataset.  Here, by genes, we refer strictly to the genomic region that produces some protein, without considering regulatory or noncoding regions that influence gene expression.  The gene name (known as symbol) can be from either of these two databases - NCBI and Ensembl.  For example, fetching details for a gene symbol:  #### PHP example ```php $geneSymbol = \"C1ORF159\"; $geneDetails = null; // check to see if you have access to the customer genetic data if (isset($productAuthorization[\"scopes\"][\"dataset\"])) {     // get all authorized SNPs within a gene     $geneDetails = $apiClient->getClientGene(         $productAuthorization[\"clientUuid\"],         $productAuthorization[\"scopes\"][\"dataset\"],         $geneSymbol     ); } ```  #### Python example ```python geneSymbol = \"C1ORF159\" geneDetails = None # check to see if you have access to the customer genetic data if hasattr(productAuthorization.scopes, \"dataset\"):     # get all authorized SNPs within a gene     geneDetails = apiClient.get_client_gene(         productAuthorization.client_uuid,         productAuthorization.scopes.dataset,         geneSymbol     ) ```  ##### All the geneDetails object attributes are  | Attribute name PHP | Attribute name Python    | Description                                                                              | |:---------------------:|:---------------------:|:-----------------------------------------------------------------------------------------| | `molecularLocation`  | `molecular_location`   | An object containing the location of the gene within the chromosome - see below the molecular location object structure  | | `snps`                | `snps`                | A list of SNP objects present in the gene - see below the SNP object structure           | | `symbol`              | `symbol`              | The gene's accession string (name)                                                       |  ##### Molecular location attributes   | Attribute name PHP     | Attribute name Python    | Description                                                                              | |:-------------------------:|:---------------------:|:-----------------------------------------------------------------------------------------| | `chromosomeAccession`    | `chromosome_accession` | The scaffold/chromosome on which the gene is placed                                      | | `start`                   | `start`               | The gene's start position on the scaffold                                                | | `stop`                    | `stop`                | The gene's stop position on the scaffold                                                 |  ##### SNP object structure  | Attribute name PHP     | Attribute name Python    | Description                                                                              | |:-------------------------:|:---------------------:|:-----------------------------------------------------------------------------------------| | `referenceGenome`        | `reference_genome`     | The reference genome known to be used by the Dataset's source. <br> This impacts the reference allele, location, and based on the dbSNP build, also the SNP's accession| | `genotypedAlleles`       | `genotyped_alleles`    | The genotype value of the customer's queried SNP. <br><br> If the attribute of this SNP has the `phased` flag set to True, <br>the first items in the lists for all SNPs will be on the same inherited chromosome, <br>and analogous for the second item. <br><br> If the SNP is unphased, the order of the items is irrelevant                                          | | `phased`                  | `phased`              | A boolean. True if the SNP is known to be phased, False otherwise                         | | `chromosomeAccession`    | `chromosome_accession` | This is the chromosome accession number where the SNP is located; in the format of NC_00x | | `location`                | `location`            | This is the customer's SNP's location on the chromosome                                   |  ## Get customer genetic data in 23andMe tsv format  If your platform is already compatible with 23andMe genotype data files, you can use this specific function to generate data in the 23andMe format - list of rows in tab separated values.  #### PHP example: ```PHP $authorizationDnaData = $apiClient->authorizationDnaData($productAuthorization[\"authorizationUuid\"]); ```  #### Python example ```python authorizationDnaData = apiClient.authorization_dna_data(productAuthorization.authorization_uuid) ```  `authorizationDnaData` contains a list of rows in a tsv (tab delimited values)/csv format (23andme-compatible)  # Submit reports  After you finish analysing the customer's genetic data, we need to inform the customer their analysis is complete. To do this, you will notify us using the function below. Finally, the customer will then:  * access their report file through a written electronic document (eg. .pdf or .doc) * access their report on your website under an account with a username and a password or * receive a physical product  ## How to submit a report file  When you submit such a report file, Lumminary will save this document into the customer's account, from which the customer will then be able to access it directly.  #### PHP example ```php $pathToReportFile = <path_to_report_file>; $fileReport = new \\SplFileObject($pathToReportFile);  $friendlyFileName = \"report_file_name\"; //optional, give a friendly name to your report file $apiClient->postAuthorizationResultFile(    $productAuthorization[\"productUuid\"],    $productAuthorization[\"authorizationUuid\"],    $fileReport,    $friendlyFileName ); ```  #### Python example ```python pathToReport = <path_to_report_file> originalFilename = \"report_file_name\" #optional, give a friendly name to your report file apiClient.post_authorization_result_file(    productAuthorization.product_uuid,    productAuthorization.authorization_uuid,    pathToReport,    originalFilename ) ```  If you need to upload multiple files, you have to call the function for each file, one at a time.   ## How to submit a report so the customer can access it on your website  If the customer's results can be accessed on your website, you will need to create a customer account on your platform, generating a user and password which will be sent through the Lumminary API into the customer's Lumminary account.   In case you don't generate a user and a password for the customer to access their report, use the function below with \"null\" value to username and password. We recommend you use the URL for customer reports on a dedicated page for reports only, rather than your homepage or some other generic page.  #### PHP example: ```php $apiClient->postAuthorizationResultCredentials(    $productAuthorization[\"productUuid\"],    $productAuthorization[\"authorizationUuid\"],    <username_generated_by_you>, //optional, default null    <password_generated_by_you>, //optional, default null    <report_on_your_website_url> // https://partnerwebsite.com/reports.php?reportid=a7508 ); ```  #### Python example: ```python apiClient.post_authorization_result_credentials(    productAuthorization.product_uuid,    productAuthorization.authorization_uuid,    <username_generated_by_you>, # optional, default null    <password_generated_by_you>, # optional, default null    <report_on_your_website_url> # https://partnerwebsite.com/reports.php?reportid=a7508 ) ```  ## How to submit a physical product In case you only send the customer a physical product and you don't generate any reports, you need to run the function below so we can mark the order as fulfilled and can inform the client.  #### PHP example: ```php $apiClient->postProductAuthorization(   $productAuthorization[\"productUuid\"],   $productAuthorization[\"authorizationUuid\"] ); ```  #### Python example: ```python apiClient.post_product_authorization(    productAuthorization.product_uuid,    productAuthorization.authorization_uuid ) ```  # The Connect with Lumminary button  The \"Connect with Lumminary\" functionality allows you to get customer details and genetic data from the Lumminary platform for free, anytime you want, for as long the customer grants you access. This functionality offers your customers the option to share their genetic data and other personal information (e.g. name, address, email etc.) stored on the Lumminary platform.   Having this button on your website makes it very easy for the customer to share their genetic data with you, as they don't have to download and re-upload their data on your site. The customer always has the option to revoke your access to both their personal details and their genetic data.  **`To protect the customer's privacy, you are not allowed to save their data anywhere. You can, however, always access their data on the Lumminary platform, for as long as they grant you access. If you generate a report based on customer data, you are allowed to save that report on your platform.`**  In order to implement this functionality on your website, this is what you need to know: * Register your product on the Lumminary platform * Add the \"Connect with Lumminary\" button to your website * Configure your website to retrieve customer data * Possible errors  ## Register your product on the Lumminary platform  If you're new to the Lumminary platform and don't already have any products in the DNA App Store, then you need to register by [filling in this form](https://lumminary.com/register-for-connect-with-lumminary).  You have to fill in the form for all products and services that require access to Lumminary customers' genetic data.    ## Add the Connect with Lumminary button to your website  Since the CWL flow involves encrypting and decrypting data, we recommend installing the Lumminary API Client, where you'll find some specific helper functions.   In order to enable the button, you have to include the following script in the `<head>` tag of all the pages where you want to enable the “Connect with Lumminary” button:  ```html <head>     <script defer src=\"https://lumminary.com/cwl/cwl.js\"></script> </head> ```  The Javascript creates a CSRF token and attaches it to the button to be transmitted and verified on our servers each time a user clicks on the button. The CSRF token expires after 5 minutes. In case the CSRF token is expired or tampered, the user will be redirected to your website where it's up to you to decide what to do next - reload the page with the button or show the customer an error message.  The `cwl.js` file is loaded as a deferred resource, which means that it will load after all the webpage code execution has been finished, so it will not have any impact on your website load speed.  ### Chose a button colour  There are two type of buttons, so you can pick one that matches your branding. The buttons are SVG images, which means that you can scale them up or down to fit your design, without compromising on image quality. You can do this by changing the image height.  ##### a. White button version   <img src=\"https://lumminary.com/cwl/connect-with-lumminary-white.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/>  <br>  ```html <a class=\"lumminary-connect-btn\" data-partner-uuid=\"<partner-UUID>\" data-request=\"<request>\" style=\"cursor:pointer; text-decoration:none;\" href=\"https://lumminary.com\">    <img src=\"https://lumminary.com/cwl/connect-with-lumminary-white.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/> </a> ```  ##### b.  Black button version  <img src=\"https://lumminary.com/cwl/connect-with-lumminary-black.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/>  <br>  ```html <a class=\"lumminary-connect-btn\" data-partner-uuid=\"<partner-UUID>\" data-request=\"<request>\" style=\"cursor:pointer; text-decoration:none;\" href=\"https://lumminary.com\">    <img src=\"https://lumminary.com/cwl/connect-with-lumminary-black.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/> </a> ```  ## Button configuration  Each button has 2 attributes which need to be configured:  1. **data-partner-uuid** where you have to add your partner UUID (you have received the partner UUID after filling in the form for product registration).  2. **data-request** which is a string obtained by encrypting a serialized JSON (you have received the CWL encryption key after filling in the form for product registration). See details below.   #### Data-request object  The data-request object has a standard format which needs to be preserved. It is formed of two types of data, some mandatory and some optional. You can use the optional fields to add any metadata or other information for your own use. The data-request object is going to be returned with the response from the authentication without being altered.  ##### Mandatory information  The mandatory information is a list of scopes which you ask the client to grant permission for. These scopes are comma delimited, and the possible options are: `address`, `email`, `dataset`.  The scopes _address_, _email_, and _dataset_ can be used in any combination; you must request at least one scope.  | Attribute name    | Description                                         | |:-----------------:|:----------------------------------------------------| | `address`         | Requests access to a customer's name and address.   | | `email`           | Requests access to a customer's email address.      | | `dataset`         | Requests access to a customer's genetic data        |  #### PHP example: ```php $objAuthorizationRequest [\"scopes\"] = \"address,dataset,email\"; ```  #### Python example: ```python objAuthorizationRequest [\"scopes\"] = \"address,dataset,email\" ```  Product UUID is your `productUuid` for which you ask customer permissions.  #### PHP example: ```php $objAuthorizationRequest[\"productUuid\"] = $credentials->getProductUuid(); ```  #### Python example: ```python objAuthorizationRequest[\"productUuid\"] = credentials.product_uuid ```  ##### Optional information  In the optional part of the object, you can add any useful data, such as customer ID,  session ID, or any parameter which can help you identify the response from Lumminary.  #### PHP example: ```php $objAuthorizationRequest[\"customData\"] = array(); $objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id>; $objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session>; $objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data>; ```  #### Python example: ```python objAuthorizationRequest[\"customData\"] = {} objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id> objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session> objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data> ```  See below a complete example for a data-request object:  #### PHP example: ```php $objAuthorizationRequest[\"scopes\"] = \"address,dataset,email\"; $objAuthorizationRequest[\"productUuid\"] = <product-UUID>;  $objAuthorizationRequest[\"customData\"] = array(); $objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id>; $objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session>; $objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data>; ```  #### Python example: ```python objAuthorizationRequest = {} objAuthorizationRequest[\"scopes\"] = \"address,dataset,email\" objAuthorizationRequest[\"productUuid\"] = <product-UUID>  objAuthorizationRequest[\"customData\"] = {} objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id> objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session> objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data> ```  ## Creating the Authorization Request  The previously generated object (`objAuthorizationRequest`) will now need to be encrypted. In order to be able to encrypt the object and also query the Lumminary API to obtain the customer details and genetic data, you need to have the Lumminary API Client installed. If you haven't done this already, please follow these [steps](#Install-Lumminary-API-Client-andor-Toolkit).  ### Add data-request attribute  After you have the Lumminary API Client installed correctly you can use the command below:  #### PHP example: ```php // You have recieved the CWL encryption key after filling in the form for product registration $partnerCwlKey = <partner-encryption-key>; $requestValueEncryptedUrlEncoded = Lumminary\\Client\\LumminaryApi::cwl_data_request_build(     $objAuthorizationRequest,     $partnerCwlKey ); ```  #### Python example: ```python import lumminary_sdk as lumminary  # You have recieved the CWL encryption key after filling in the form for product partnerCwlKey = <partner-encryption-key>  requestValueEncryptedUrlEncoded = lumminary.LumminaryApi.cwl_data_request_build(objAuthorizationRequest, partnerCwlKey) ```  The resulting string should be added in the `data-request` attribute of the `<a>` tag of the \"Connect with Lumminary\" button.  ### Add data-partner-uuid attribute  Add the `data-partner-uuid` in the `data-partner-uuid` attribute of the `<a>` tag of the \"Connect with Lumminary\" button. You have received the partner UUID after filling in the form for product registration.  An example of a button correctly configured should look like this:  ```html <a class=\"lumminary-connect-btn\" data-partner-uuid=\"4231-7446-2543-6542\" data-request=\"7LfMX811Als0l%2FAvf84pB7n3mcycnTjgWl1FaVNffdqiOApMn4HAnk0Ux6eatObfYmxf1xPRjo7nBojsL4ImgOL932NK2Ei4VoUXjs9Y%2BcvphI0kxBSblLaeVXNPbJO9LsuNP%2BHJzDBAnZZdAObgYxHH2QDY3VD%2Ff%2FBXKw9WYDdBssAoegMFEJ9GgYutFQ4nTPXAt%2FdWCqoxYbZrYpCj2Pphk9lstc4Ib%2BLNxKiEtNCmVGr6sgmR2lPBwgylTsEX%2FMRCJb6sdQyZBhvSQCMFb0p3%2B9tEwV0%3D\" style=\"cursor:pointer; text-decoration:none;\" href=\"https://lumminary.com\">    <img src=\"https://lumminary.com/cwl/connect-with-lumminary-white.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"> </a> ```  ## Connect with Lumminary summary of user interaction  When a customer clicks on the “Connect with Lumminary” button, a pop-up window opens. After they choose which genetic file to share, the pop-up will automatically close and the user will be redirected to your callback URL in the parent window. Your callback URL needs to be predefined in the Lumminary partner portal.   The GET request from the client to your callback URL will contain two querystring parameters - `request` and `response`:  1. `request` – this is exactly the same request that you previously sent in the `data-request` field. You can decrypt it with the CWL encryption key which you used to encrypt it. 2. `response` – the response is an urlencoded encrypted serialized JSON object which contains the Authorization UUID and the Authorization UTC unix timestamp. You will use the Authorization UUID to get the customer's data with the Lumminary API Client. The response string is encrypted with your CWL encryption key, the same as the `data-request` parameter.   In order to decrypt the `response` parameter, you can use the following function:  #### PHP example: ```php // the entire callback URL, including the querystring parameters $callbackUrlWithPayload = \"https://partnerwebsite.con/callback?request=...&response=...\";  $cwlReturnObject = Lumminary\\Client\\LumminaryApi::cwl_url_query_extract(     $callbackUrlWithPayload,      $partnerCwlKey   ); ```  #### Python example: ```python // the entire callback URL, including the querystring parameters callback_url_with_payload = \"https://partnerwebsite.con/callback?request=...&response=...\"  cwlReturnObject = apiClient.cwl_url_query_extract(     callback_url_with_payload,     partner_cwl_key ) ```  The `cwlReturnObject` will now contain an object like the example below:  ```json {     \"request\": <your-request-parameter-echoed>,     \"response\": {         \"authorizationUuid\": <cwl-authorization-uuid>,         \"authorizationTimestamp\": <cwl-authorization-created-timestamp>     } } ```  With the Authorization UUID (`authorizationUuid`) you can [query all the customer details](#Query-customer-genetic-data) from the Lumminary platform.  ## Possible errors  When an error occurs, the customer is redirected to your callback URL. The redirect contains two querystring parameters - `request` and `response` - exactly like a regular response, but the `response` parameter contains an error object (see below) instead of an Authorization object.  #### PHP example: ```php // the entire callback url, including the querystring parameters $callbackUrlWithPayload = \"https://partnerwebsite.con/callback?request=...&response=...\";  $cwlReturnObject = Lumminary\\Client\\LumminaryApi::cwl_url_query_extract(     $callbackUrlWithPayload,      $partnerCwlKey   ); ```  #### Python example: ```python # the entire callback url, including the querystring parameters callback_url_with_payload = \"https://partnerwebsite.con/callback?request=...&response=...\"  cwlReturnObject = apiClient.cwl_url_query_extract(     callback_url_with_payload,     partner_cwl_key ) ```  Example of a return object (`cwlReturnObject`) containing an error message:  ```json {     \"request\": <your-request-parameter-echoed>,     \"response\": {         \"error\": {             \"id\": <error id>,             \"message\": <error message>         }     } } ```  | Error Id          | Error Message                                                                                | |:-----------------:|:---------------------------------------------------------------------------------------------| | 1                 | Invalid Security Token                                                                       | | 2                 | Invalid Access Scopes                                                                        | | 3                 | Customer refuses your request (this happens when the customer cancels instead of granting access) |
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILumminaryAPISpecApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAILumminaryAPISpecApi::OAILumminaryAPISpecApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAILumminaryAPISpecApi::~OAILumminaryAPISpecApi() {
}

void OAILumminaryAPISpecApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("//api.lumminary.com/v1"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("getAuthorizationsQueue", defaultConf);
    _serverIndices.insert("getAuthorizationsQueue", 0);
    _serverConfigs.insert("getClientGene", defaultConf);
    _serverIndices.insert("getClientGene", 0);
    _serverConfigs.insert("getClientSnp", defaultConf);
    _serverIndices.insert("getClientSnp", 0);
    _serverConfigs.insert("getClientSnpGroup", defaultConf);
    _serverIndices.insert("getClientSnpGroup", 0);
    _serverConfigs.insert("getGene", defaultConf);
    _serverIndices.insert("getGene", 0);
    _serverConfigs.insert("getProduct", defaultConf);
    _serverIndices.insert("getProduct", 0);
    _serverConfigs.insert("getProductAuthorization", defaultConf);
    _serverIndices.insert("getProductAuthorization", 0);
    _serverConfigs.insert("getReferenceChromosome", defaultConf);
    _serverIndices.insert("getReferenceChromosome", 0);
    _serverConfigs.insert("getReferenceGenome", defaultConf);
    _serverIndices.insert("getReferenceGenome", 0);
    _serverConfigs.insert("getReferenceGenomesGroup", defaultConf);
    _serverIndices.insert("getReferenceGenomesGroup", 0);
    _serverConfigs.insert("getReferenceSnp", defaultConf);
    _serverIndices.insert("getReferenceSnp", 0);
    _serverConfigs.insert("postAuthorizationResultCredentials", defaultConf);
    _serverIndices.insert("postAuthorizationResultCredentials", 0);
    _serverConfigs.insert("postAuthorizationResultFile", defaultConf);
    _serverIndices.insert("postAuthorizationResultFile", 0);
    _serverConfigs.insert("postClientSnpGroup", defaultConf);
    _serverIndices.insert("postClientSnpGroup", 0);
    _serverConfigs.insert("postJwtAuth", defaultConf);
    _serverIndices.insert("postJwtAuth", 0);
    _serverConfigs.insert("postProductAuthorization", defaultConf);
    _serverIndices.insert("postProductAuthorization", 0);
    _serverConfigs.insert("postProductAuthorizationUnfulfillable", defaultConf);
    _serverIndices.insert("postProductAuthorizationUnfulfillable", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAILumminaryAPISpecApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAILumminaryAPISpecApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAILumminaryAPISpecApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAILumminaryAPISpecApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAILumminaryAPISpecApi::setUsername(const QString &username) {
    _username = username;
}

void OAILumminaryAPISpecApi::setPassword(const QString &password) {
    _password = password;
}


void OAILumminaryAPISpecApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAILumminaryAPISpecApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAILumminaryAPISpecApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAILumminaryAPISpecApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAILumminaryAPISpecApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAILumminaryAPISpecApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAILumminaryAPISpecApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAILumminaryAPISpecApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAILumminaryAPISpecApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAILumminaryAPISpecApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAILumminaryAPISpecApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAILumminaryAPISpecApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAILumminaryAPISpecApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAILumminaryAPISpecApi::getAuthorizationsQueue(const QString &product_id, const ::OpenAPI::OptionalParam<QString> &seq_num_start, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getAuthorizationsQueue"][_serverIndices.value("getAuthorizationsQueue")].URL()+"/products/{productId}/authorizations");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString product_idPathParam("{");
        product_idPathParam.append("productId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "productId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"productId"+pathSuffix : pathPrefix;
        fullPath.replace(product_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(product_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (seq_num_start.hasValue())
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "seq_num_start", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("seq_num_start")).append(querySuffix).append(QUrl::toPercentEncoding(seq_num_start.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getAuthorizationsQueueCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getAuthorizationsQueueCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIAuthorization> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIAuthorization val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getAuthorizationsQueueSignal(output);
        Q_EMIT getAuthorizationsQueueSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getAuthorizationsQueueSignalE(output, error_type, error_str);
        Q_EMIT getAuthorizationsQueueSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getAuthorizationsQueueSignalError(output, error_type, error_str);
        Q_EMIT getAuthorizationsQueueSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getClientGene(const QString &client_id, const QString &dataset_id, const QString &gene_symbol, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getClientGene"][_serverIndices.value("getClientGene")].URL()+"/clients/{clientId}/datasets/{datasetId}/genes/{geneSymbol}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString client_idPathParam("{");
        client_idPathParam.append("clientId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "clientId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"clientId"+pathSuffix : pathPrefix;
        fullPath.replace(client_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(client_id)));
    }
    
    {
        QString dataset_idPathParam("{");
        dataset_idPathParam.append("datasetId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "datasetId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"datasetId"+pathSuffix : pathPrefix;
        fullPath.replace(dataset_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dataset_id)));
    }
    
    {
        QString gene_symbolPathParam("{");
        gene_symbolPathParam.append("geneSymbol").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "geneSymbol", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"geneSymbol"+pathSuffix : pathPrefix;
        fullPath.replace(gene_symbolPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(gene_symbol)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getClientGeneCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getClientGeneCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIClientGene output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getClientGeneSignal(output);
        Q_EMIT getClientGeneSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getClientGeneSignalE(output, error_type, error_str);
        Q_EMIT getClientGeneSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getClientGeneSignalError(output, error_type, error_str);
        Q_EMIT getClientGeneSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getClientSnp(const QString &client_id, const QString &dataset_id, const QString &snp_id, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getClientSnp"][_serverIndices.value("getClientSnp")].URL()+"/clients/{clientId}/datasets/{datasetId}/snps/{snpId}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString client_idPathParam("{");
        client_idPathParam.append("clientId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "clientId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"clientId"+pathSuffix : pathPrefix;
        fullPath.replace(client_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(client_id)));
    }
    
    {
        QString dataset_idPathParam("{");
        dataset_idPathParam.append("datasetId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "datasetId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"datasetId"+pathSuffix : pathPrefix;
        fullPath.replace(dataset_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dataset_id)));
    }
    
    {
        QString snp_idPathParam("{");
        snp_idPathParam.append("snpId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "snpId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"snpId"+pathSuffix : pathPrefix;
        fullPath.replace(snp_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(snp_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getClientSnpCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getClientSnpCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIClientSNP output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getClientSnpSignal(output);
        Q_EMIT getClientSnpSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getClientSnpSignalE(output, error_type, error_str);
        Q_EMIT getClientSnpSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getClientSnpSignalError(output, error_type, error_str);
        Q_EMIT getClientSnpSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getClientSnpGroup(const QString &client_id, const QString &dataset_id, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getClientSnpGroup"][_serverIndices.value("getClientSnpGroup")].URL()+"/clients/{clientId}/datasets/{datasetId}/snps/");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString client_idPathParam("{");
        client_idPathParam.append("clientId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "clientId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"clientId"+pathSuffix : pathPrefix;
        fullPath.replace(client_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(client_id)));
    }
    
    {
        QString dataset_idPathParam("{");
        dataset_idPathParam.append("datasetId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "datasetId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"datasetId"+pathSuffix : pathPrefix;
        fullPath.replace(dataset_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dataset_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getClientSnpGroupCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getClientSnpGroupCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIClientSNP> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIClientSNP val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getClientSnpGroupSignal(output);
        Q_EMIT getClientSnpGroupSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getClientSnpGroupSignalE(output, error_type, error_str);
        Q_EMIT getClientSnpGroupSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getClientSnpGroupSignalError(output, error_type, error_str);
        Q_EMIT getClientSnpGroupSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getGene(const QString &database_name, const QString &accession, const ::OpenAPI::OptionalParam<qint32> &dbsnp_build, const ::OpenAPI::OptionalParam<QString> &reference_genome, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getGene"][_serverIndices.value("getGene")].URL()+"/reference/genes/databases/{databaseName}/accessions/{accession}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString database_namePathParam("{");
        database_namePathParam.append("databaseName").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "databaseName", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"databaseName"+pathSuffix : pathPrefix;
        fullPath.replace(database_namePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(database_name)));
    }
    
    {
        QString accessionPathParam("{");
        accessionPathParam.append("accession").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "accession", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"accession"+pathSuffix : pathPrefix;
        fullPath.replace(accessionPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(accession)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (dbsnp_build.hasValue())
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "dbsnp_build", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("dbsnp_build")).append(querySuffix).append(QUrl::toPercentEncoding(dbsnp_build.stringValue()));
    }
    if (reference_genome.hasValue())
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "reference_genome", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("reference_genome")).append(querySuffix).append(QUrl::toPercentEncoding(reference_genome.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getGeneCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getGeneCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPublicGene output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getGeneSignal(output);
        Q_EMIT getGeneSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getGeneSignalE(output, error_type, error_str);
        Q_EMIT getGeneSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getGeneSignalError(output, error_type, error_str);
        Q_EMIT getGeneSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getProduct(const QString &product_id, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getProduct"][_serverIndices.value("getProduct")].URL()+"/products/{productId}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString product_idPathParam("{");
        product_idPathParam.append("productId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "productId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"productId"+pathSuffix : pathPrefix;
        fullPath.replace(product_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(product_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getProductCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getProductCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIProduct output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getProductSignal(output);
        Q_EMIT getProductSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getProductSignalE(output, error_type, error_str);
        Q_EMIT getProductSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getProductSignalError(output, error_type, error_str);
        Q_EMIT getProductSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getProductAuthorization(const QString &product_id, const QString &authorization_id, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getProductAuthorization"][_serverIndices.value("getProductAuthorization")].URL()+"/products/{productId}/authorizations/{authorizationId}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString product_idPathParam("{");
        product_idPathParam.append("productId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "productId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"productId"+pathSuffix : pathPrefix;
        fullPath.replace(product_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(product_id)));
    }
    
    {
        QString authorization_idPathParam("{");
        authorization_idPathParam.append("authorizationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "authorizationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"authorizationId"+pathSuffix : pathPrefix;
        fullPath.replace(authorization_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(authorization_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getProductAuthorizationCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getProductAuthorizationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAuthorization output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getProductAuthorizationSignal(output);
        Q_EMIT getProductAuthorizationSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getProductAuthorizationSignalE(output, error_type, error_str);
        Q_EMIT getProductAuthorizationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getProductAuthorizationSignalError(output, error_type, error_str);
        Q_EMIT getProductAuthorizationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getReferenceChromosome(const QString &genome_build_accession, const QString &chromosome_accession, const qint32 &range_start, const qint32 &range_stop, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getReferenceChromosome"][_serverIndices.value("getReferenceChromosome")].URL()+"/reference/genomes/{genomeBuildAccession}/chromosomes/{chromosomeAccession}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString genome_build_accessionPathParam("{");
        genome_build_accessionPathParam.append("genomeBuildAccession").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "genomeBuildAccession", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"genomeBuildAccession"+pathSuffix : pathPrefix;
        fullPath.replace(genome_build_accessionPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(genome_build_accession)));
    }
    
    {
        QString chromosome_accessionPathParam("{");
        chromosome_accessionPathParam.append("chromosomeAccession").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "chromosomeAccession", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"chromosomeAccession"+pathSuffix : pathPrefix;
        fullPath.replace(chromosome_accessionPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(chromosome_accession)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range_start", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("range_start")).append(querySuffix).append(QUrl::toPercentEncoding(range_start));
    }
    
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "range_stop", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("range_stop")).append(querySuffix).append(QUrl::toPercentEncoding(range_stop));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getReferenceChromosomeCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getReferenceChromosomeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIReferenceSequence output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getReferenceChromosomeSignal(output);
        Q_EMIT getReferenceChromosomeSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getReferenceChromosomeSignalE(output, error_type, error_str);
        Q_EMIT getReferenceChromosomeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getReferenceChromosomeSignalError(output, error_type, error_str);
        Q_EMIT getReferenceChromosomeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getReferenceGenome(const QString &genome_build_accession, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getReferenceGenome"][_serverIndices.value("getReferenceGenome")].URL()+"/reference/genomes/{genomeBuildAccession}/chromosomes");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString genome_build_accessionPathParam("{");
        genome_build_accessionPathParam.append("genomeBuildAccession").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "genomeBuildAccession", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"genomeBuildAccession"+pathSuffix : pathPrefix;
        fullPath.replace(genome_build_accessionPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(genome_build_accession)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getReferenceGenomeCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getReferenceGenomeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIReferenceChromosomeOverview> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIReferenceChromosomeOverview val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getReferenceGenomeSignal(output);
        Q_EMIT getReferenceGenomeSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getReferenceGenomeSignalE(output, error_type, error_str);
        Q_EMIT getReferenceGenomeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getReferenceGenomeSignalError(output, error_type, error_str);
        Q_EMIT getReferenceGenomeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getReferenceGenomesGroup(const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getReferenceGenomesGroup"][_serverIndices.value("getReferenceGenomesGroup")].URL()+"/reference/genomes/");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getReferenceGenomesGroupCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getReferenceGenomesGroupCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIReferenceGenomeOverview> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIReferenceGenomeOverview val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getReferenceGenomesGroupSignal(output);
        Q_EMIT getReferenceGenomesGroupSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getReferenceGenomesGroupSignalE(output, error_type, error_str);
        Q_EMIT getReferenceGenomesGroupSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getReferenceGenomesGroupSignalError(output, error_type, error_str);
        Q_EMIT getReferenceGenomesGroupSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::getReferenceSnp(const QString &snp_accession, const ::OpenAPI::OptionalParam<qint32> &dbsnp_version, const ::OpenAPI::OptionalParam<QString> &grch_version, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["getReferenceSnp"][_serverIndices.value("getReferenceSnp")].URL()+"/reference/snps/{snpAccession}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString snp_accessionPathParam("{");
        snp_accessionPathParam.append("snpAccession").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "snpAccession", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"snpAccession"+pathSuffix : pathPrefix;
        fullPath.replace(snp_accessionPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(snp_accession)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (dbsnp_version.hasValue())
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "dbsnp_version", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("dbsnp_version")).append(querySuffix).append(QUrl::toPercentEncoding(dbsnp_version.stringValue()));
    }
    if (grch_version.hasValue())
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "grch_version", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("grch_version")).append(querySuffix).append(QUrl::toPercentEncoding(grch_version.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::getReferenceSnpCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::getReferenceSnpCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPublicSNP output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getReferenceSnpSignal(output);
        Q_EMIT getReferenceSnpSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getReferenceSnpSignalE(output, error_type, error_str);
        Q_EMIT getReferenceSnpSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getReferenceSnpSignalError(output, error_type, error_str);
        Q_EMIT getReferenceSnpSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::postAuthorizationResultCredentials(const QString &product_id, const QString &authorization_id, const ::OpenAPI::OptionalParam<QString> &x_fields, const ::OpenAPI::OptionalParam<QString> &credentials_username, const ::OpenAPI::OptionalParam<QString> &credentials_password, const ::OpenAPI::OptionalParam<QString> &report_url) {
    QString fullPath = QString(_serverConfigs["postAuthorizationResultCredentials"][_serverIndices.value("postAuthorizationResultCredentials")].URL()+"/products/{productId}/authorizations/{authorizationId}/credentials");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString product_idPathParam("{");
        product_idPathParam.append("productId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "productId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"productId"+pathSuffix : pathPrefix;
        fullPath.replace(product_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(product_id)));
    }
    
    {
        QString authorization_idPathParam("{");
        authorization_idPathParam.append("authorizationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "authorizationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"authorizationId"+pathSuffix : pathPrefix;
        fullPath.replace(authorization_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(authorization_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (credentials_username.hasValue())
    {
        input.add_var("credentials_username", ::OpenAPI::toStringValue(credentials_username.value()));
    }
    if (credentials_password.hasValue())
    {
        input.add_var("credentials_password", ::OpenAPI::toStringValue(credentials_password.value()));
    }
    if (report_url.hasValue())
    {
        input.add_var("report_url", ::OpenAPI::toStringValue(report_url.value()));
    }

    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::postAuthorizationResultCredentialsCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::postAuthorizationResultCredentialsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIReportCredentials output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postAuthorizationResultCredentialsSignal(output);
        Q_EMIT postAuthorizationResultCredentialsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT postAuthorizationResultCredentialsSignalE(output, error_type, error_str);
        Q_EMIT postAuthorizationResultCredentialsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postAuthorizationResultCredentialsSignalError(output, error_type, error_str);
        Q_EMIT postAuthorizationResultCredentialsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::postAuthorizationResultFile(const QString &product_id, const QString &authorization_id, const ::OpenAPI::OptionalParam<QString> &original_filename, const ::OpenAPI::OptionalParam<QString> &x_fields, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &file_report) {
    QString fullPath = QString(_serverConfigs["postAuthorizationResultFile"][_serverIndices.value("postAuthorizationResultFile")].URL()+"/products/{productId}/authorizations/{authorizationId}/file");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString product_idPathParam("{");
        product_idPathParam.append("productId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "productId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"productId"+pathSuffix : pathPrefix;
        fullPath.replace(product_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(product_id)));
    }
    
    {
        QString authorization_idPathParam("{");
        authorization_idPathParam.append("authorizationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "authorizationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"authorizationId"+pathSuffix : pathPrefix;
        fullPath.replace(authorization_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(authorization_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (original_filename.hasValue())
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "original_filename", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("original_filename")).append(querySuffix).append(QUrl::toPercentEncoding(original_filename.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (file_report.hasValue())
    {
        input.add_file("file_report", file_report.value().local_filename, file_report.value().request_filename, file_report.value().mime_type);
    }

    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::postAuthorizationResultFileCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::postAuthorizationResultFileCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIReportFile output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postAuthorizationResultFileSignal(output);
        Q_EMIT postAuthorizationResultFileSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT postAuthorizationResultFileSignalE(output, error_type, error_str);
        Q_EMIT postAuthorizationResultFileSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postAuthorizationResultFileSignalError(output, error_type, error_str);
        Q_EMIT postAuthorizationResultFileSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::postClientSnpGroup(const QString &client_id, const QString &dataset_id, const QString &snps, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["postClientSnpGroup"][_serverIndices.value("postClientSnpGroup")].URL()+"/clients/{clientId}/datasets/{datasetId}/snps/");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString client_idPathParam("{");
        client_idPathParam.append("clientId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "clientId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"clientId"+pathSuffix : pathPrefix;
        fullPath.replace(client_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(client_id)));
    }
    
    {
        QString dataset_idPathParam("{");
        dataset_idPathParam.append("datasetId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "datasetId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"datasetId"+pathSuffix : pathPrefix;
        fullPath.replace(dataset_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(dataset_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    
    {
        input.add_var("snps", ::OpenAPI::toStringValue(snps));
    }

    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::postClientSnpGroupCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::postClientSnpGroupCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIClientSNP> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIClientSNP val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postClientSnpGroupSignal(output);
        Q_EMIT postClientSnpGroupSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT postClientSnpGroupSignalE(output, error_type, error_str);
        Q_EMIT postClientSnpGroupSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postClientSnpGroupSignalError(output, error_type, error_str);
        Q_EMIT postClientSnpGroupSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::postJwtAuth(const QString &username, const QString &password, const QString &role, const ::OpenAPI::OptionalParam<QString> &x_fields) {
    QString fullPath = QString(_serverConfigs["postJwtAuth"][_serverIndices.value("postJwtAuth")].URL()+"/auth/jwt");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    
    {
        input.add_var("username", ::OpenAPI::toStringValue(username));
    }
    
    {
        input.add_var("password", ::OpenAPI::toStringValue(password));
    }
    
    {
        input.add_var("role", ::OpenAPI::toStringValue(role));
    }

    if (x_fields.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_fields.value()).isEmpty()) {
            input.headers.insert("X-Fields", ::OpenAPI::toStringValue(x_fields.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::postJwtAuthCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::postJwtAuthCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIJavascriptWebToken output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postJwtAuthSignal(output);
        Q_EMIT postJwtAuthSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT postJwtAuthSignalE(output, error_type, error_str);
        Q_EMIT postJwtAuthSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postJwtAuthSignalError(output, error_type, error_str);
        Q_EMIT postJwtAuthSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::postProductAuthorization(const QString &product_id, const QString &authorization_id) {
    QString fullPath = QString(_serverConfigs["postProductAuthorization"][_serverIndices.value("postProductAuthorization")].URL()+"/products/{productId}/authorizations/{authorizationId}");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString product_idPathParam("{");
        product_idPathParam.append("productId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "productId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"productId"+pathSuffix : pathPrefix;
        fullPath.replace(product_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(product_id)));
    }
    
    {
        QString authorization_idPathParam("{");
        authorization_idPathParam.append("authorizationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "authorizationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"authorizationId"+pathSuffix : pathPrefix;
        fullPath.replace(authorization_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(authorization_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::postProductAuthorizationCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::postProductAuthorizationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postProductAuthorizationSignal();
        Q_EMIT postProductAuthorizationSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT postProductAuthorizationSignalE(error_type, error_str);
        Q_EMIT postProductAuthorizationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postProductAuthorizationSignalError(error_type, error_str);
        Q_EMIT postProductAuthorizationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::postProductAuthorizationUnfulfillable(const QString &product_id, const QString &authorization_id) {
    QString fullPath = QString(_serverConfigs["postProductAuthorizationUnfulfillable"][_serverIndices.value("postProductAuthorizationUnfulfillable")].URL()+"/products/{productId}/authorizations/{authorizationId}/unfulfillable");
    
    if (_apiKeys.contains("Bearer")) {
        addHeaders("Bearer",_apiKeys.find("Bearer").value());
    }
    
    
    {
        QString product_idPathParam("{");
        product_idPathParam.append("productId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "productId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"productId"+pathSuffix : pathPrefix;
        fullPath.replace(product_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(product_id)));
    }
    
    {
        QString authorization_idPathParam("{");
        authorization_idPathParam.append("authorizationId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "authorizationId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"authorizationId"+pathSuffix : pathPrefix;
        fullPath.replace(authorization_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(authorization_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILumminaryAPISpecApi::postProductAuthorizationUnfulfillableCallback);
    connect(this, &OAILumminaryAPISpecApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILumminaryAPISpecApi::postProductAuthorizationUnfulfillableCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postProductAuthorizationUnfulfillableSignal();
        Q_EMIT postProductAuthorizationUnfulfillableSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT postProductAuthorizationUnfulfillableSignalE(error_type, error_str);
        Q_EMIT postProductAuthorizationUnfulfillableSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postProductAuthorizationUnfulfillableSignalError(error_type, error_str);
        Q_EMIT postProductAuthorizationUnfulfillableSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILumminaryAPISpecApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
