/*
 * Lumminary API
 * # Introduction The Lumminary API was built to allow third parties to interact with Lumminary customers and gain access to their genetic data. The Lumminary API is fast, scalable and highly secure. All requests to the Lumminary API take place over SSL, which means all communication of Customer data is encrypted.  Before we dive in, some definitions. This is what we mean by:  |Term|Definition| |-----------|-----------| |**Third party**|A third party (also referred to as \"partner\" or as \"you\") is a company which offers services and products using genetic data.| |**Lumminary clients**|The Lumminary client (also referred to as \"customer\") is an individual who has created an account on the Lumminary platform.| |**Lumminary**|This is  us - our services including the Lumminary platform, the API, the DNA App Store, the DNA Vault, the \"Connect with Lumminary\" button, and the website in its totality. | |**CWL**|This is the acronym for the \"Connect with Lumminary\" button.| |**dataset**|This is the term we use when we refer to a customer's genetic data.| |**Lumminary API**|This is a library/module that you can use to integrate your apps with the Lumminary platform.| |**Lumminary toolkit**|This is a stand alone application which helps you integrate with Lumminary without writing any code or interacting with the Lumminary API.|  Let's dive in, now.  * [**Overview**](#section/Introduction/Overview)  * [**Install Lumminary API Client and Toolkit**](#Install-Lumminary-API-Client-andor-Toolkit) * [**Obtaining credentials**](#Obtaining-credentials) * [**Query customers authorizations**](#Query-customers-authorizations) * [**Query customer genetic data**](#Query-customer-genetic-data) * [**Submit reports**](#Submit-reports)  * [**\"Connect with Lumminary\" button**](#the-connect-with-lumminary-button)  * [**API specs**](#tag/Lumminary)  ## Overview  In order to use Lumminary services, you'll need to install the Lumminary API Client or Toolkit. The Lumminary API Client and Toolkit are available in multiple programming languages, and we also provide a sandbox environment which you can use for integration and tests.  There are a couple of differences between the API Client and the Toolkit. Mainly, it's about the ease of use for integration. The Toolkit is basically a stand-alone application that facilitates the integration with the Lumminary API without the need to modify your already existing code.  You use the Lumminary API Client when you want to integrate it inside your own application. This means it gives you full flexibility regarding the integration into your own workflow.  You use the Lumminary Toolkit for an integration where the Toolkit is placed alongside your own application. You can use the Toolkit from the CLI - for example, to run a cronjob that processes incoming orders. The Toolkit uses the Lumminary API Client.  # Install Lumminary API Client and/or Toolkit  We provide the Lumminary API Client and Toolkit in multiple programming languages - default are PHP (minimum version 7.0), Python2.7 and Python3. However, if you need them in another language (Java, Obj-C, JavaScript, C#, Perl, CURL), please contact us.   ## How to install the Lumminary API Client  #### PHP example: The PHP Lumminary API Client is available at: https://github.com/Lumminary/lumminary-api-client-php  If you are already using [Composer](https://getcomposer.org), you can import the project by adding the following to your `composer.json` ```json \"repositories\": [     {         \"type\": \"git\",         \"url\": \"https://github.com/Lumminary/lumminary-api-client-php.git\",         \"reference\": \"master\"     } ], \"require\": {     \"lumminary/api-client-php\": \"v1.0.6\" } ```  Then run `composer update lumminary/api-client-php`  #### Python example:  The Python Lumminary API Client is available at: https://github.com/Lumminary/lumminary-api-client-python  To install directly, run  ```bash pip install git+https://git@github.com/Lumminary/lumminary-api-client-python.git@v1.0.7#egg=lumminary-api-client ```  Or add the following line in your requirements.txt  ```bash git+https://git@github.com/Lumminary/lumminary-api-client-python.git@v1.0.7#egg=lumminary-api-client ```  ## How to install the Lumminary Toolkit  #### PHP example: The PHP Lumminary Toolkit is available at: https://github.com/Lumminary/lumminary-toolkit-php  To install the Lumminary Toolkit, run the following command where 'lumminary-toolkit-directory' is the directory where you want to install the Lumminary Toolkit:  `git clone git@github.com:Lumminary/lumminary-toolkit-php.git lumminary-toolkit-directory`  #### PYTHON example:  The Python Lumminary Toolkit is available at: https://github.com/Lumminary/lumminary-toolkit-python  To install the Lumminary Toolkit, run the following command where 'lumminary-toolkit-directory' is the directory where you want to install the Lumminary Toolkit:  ```bash git clone git@github.com:Lumminary/lumminary-toolkit-python.git lumminary-toolkit-directory cd lumminary-toolkit-directory virtualenv env source env/bin/activate pip install -r requirements.txt ```  Note that before running the toolkit, you should have the virtualenv enabled, like so : `source lumminary-toolkit-directory/env/bin/activate`  ## Toolkit Setup  We recommend to run the Toolkit in a cronjob; at every run it will check for new Authorizations (Orders) and will download them; afterwards it will check for a new reports folder inside the old authorizations, process the reports, and delete the processed Authorizations and Reports from your server.   The first step after you clone the Lumminary Toolkit project for your language is to configure it with your credentials.   Go to the Lumminary Toolkit base diretory `cd lumminary-toolkit-directory`. Under the Toolkit directory, you will find a file `config/config_template.json` which has the following structure:  ```json {     \"api_key\": <your-api-key>,     \"product_uuid\": <your-product-uuid>,     \"api_host\": \"https://api.lumminary.com/v1\",     \"output_root\": <your-authorization-data-basepath>,     \"export_handler\": <your-export-handler-class>,     \"product_name\": <your-product-name>,     \"operations\": [         \"pull_datasets\",         \"push_reports\"     ],     \"optional\": {         \"dna_data_filename\": \"dna-data.tsv\",         \"authorization_metadata_filename\": \"authorization-metadata.json\"     } } ```  You should copy this config `cp config/config_template.json config/my-product1-config.json` then edit it `vim config/my-product1-config.json` to contain the following values:  | Config attribute | Example Value                      | Description | |------------------|------------------------------------|-------------| | api_key        | `\"TiiU...bqg==\"`                   |Your Lumminary API key.<br> You can obtain it from the Lumminary Admin  | | product_uuid   | `\"1234-1234-1234-1234\"`            |Your product UUID. This value can be obtained from the Lumminary Admin | | api_host       | `\"https://api.lumminary.com/v1\"`   |   The API endpoint to use.<br>For the sandbox environment you can use \"https://sandbox-api.lumminary.com/v1\"    | | output_root    | `\"/var/lumminary-orders/product1/\"`         | The base directory where the Toolkit places the Authorizations for your Product <br> The Lumminary Toolkit will *never* overwrite Authorization data or create this directory, to protect from overwrites or typos    | | export_handler |`\"export_handler_tsv\"`  | If you have a custom export handler, then your Lumminary contact will provide you with the name of your export handler.   | | operations       |`[\"pull_datasets\", \"push_reports\"]`        | These are two optional parameters that define the tasks that the Toolkit should perform. Possible values are: <br> 1. `pull_datasets` - this tells the Toolkit to download the Customer Authorization (Customer details and genetic data) <br> 2. `push_reports` - this tells the Toolkit to push the results to the API; see below for more details| | optional       | `{}`                               | Export handler specific value |  After updating the config file for your Toolkit, it should look similar to (Note that these are all dummy values) :  ```json {     \"api_key\": \"TiiU...bqg==\",     \"product_uuid\": \"1234-1234-1234-1234\",     \"api_host\": \"https://api.lumminary.com/v1\",     \"output_root\": \"/var/lumminary-orders/product1/\",     \"export_handler\": \"export_handler_tsv\",     \"product_name\": \"product 1\",     \"operations\": [         \"pull_datasets\",         \"push_reports\"     ],     \"optional\": {         \"dna_data_filename\": \"dna-data.tsv\",         \"authorization_metadata_filename\": \"authorization-metadata.json\"     } } ```  You can now save and exit the text editor `:wq` and start polling the API for new Authorizations :  Python  ```bash # While still in the <lumminary-toolkit> directory source env/bin/activate; python lumminary_partner_toolkit.py --config-path config/my-lumminary-product1-config.json ```  PHP  ```bash # While still in the <lumminary-toolkit> directory php lumminary-partner-toolkit.php --config-path config/my-lumminary-product1-config.json ```  When your Product receives new Authorizations, the Toolkit will pull all the relevant data and save it in the following files:  ```bash # The DNA data file. Format compatible with 23AndMe by default <output_root>/<authorization_uuid>/dna-data.tsv  # The Authorization metadata <output_root>/<authorization_uuid>/authorization.json ```  The contents of the files pulled when processing an Authorization are as follows:  ```bash $ head -n 5 <output_root>/<authorization_uuid>/dna-data.tsv # rsid      chromosome  position        genotype rs12070387  1           6267531         CC rs149124387 1           12025561        CC rs116458387 1           14920119        AA rs4436387   1           15498452        CC  $ cat <output_root>/<authorization_uuid>/authorization.json  {     \"authorization\": <authorization_uuid>,     \"created_timestamp_utc\": 1542920184,     \"customer\": <customer_uuid>,     \"customer_address\": {         \"address1\": <address1>,         \"address2\": <address2>,         \"city\": <city>,         \"country\": <country>,         \"state\": <state>,         \"zipcode\": <zipcode>      },     \"customer_email\": <customer_email>,     \"customer_name\": {         \"first_name\": <customer_first_name>,         \"last_name\": <customer_last_name>     },     \"dataset\": <dataset_uuid>,     \"product\": <your_product_uuid> } ```  After the Toolkit downloaded the Authorizations, you need to process the Customer genetic data file and the Customer details, individually. The Lumminary API supports multiple types of products:  | Scenario | How to Report |                     |------------------|------------------------------------| |The product is a file (.pdf, .jpeg etc.) | Put the result file(s) into the `tmp_reports` directory. Please refer to the Note underneath this table. | |The product requires authentication | Create a file with the name `result.json` into the `tmp_reports` directory, with the following content: <br> `{ \"credentials\": { \"username\": \"username@example.com\", \"password\": \"your generated password\", \"url\": \"https://your-website.com/report\"}}`<br> The `url` should point to a login page that upon authentication redirects the user to the report page. You can find the customer's email address in the `authorization-metadata.json` and the `password` attribute must be a secure password. Please refer to the Note underneath this table. | |The product is a physical product| Create a file with the name `result.json` into the `tmp_reports` directory, with the following content: <br> `{\"physical_product\": { \"physical_product_completed\": true }}` <br> This should be done upon dispatch. Please refer to the Note underneath this table. | |An error occurred| Create a file with the name `result.json` into the `tmp_reports` directory, with the following content: <br> `{ \"unfulfillable\": {\"error\": \"Reasons for why it is unfulfillable\", }}` <br> The error message is for Lumminary internal usage, and it won't be visible to the customer. This will delete your Authorization, making it unuseable thereafter. So please use this only for unfixable errors, and never for temporary errors you attempt to resolve. Please refer to the Note underneath this table. |  ###### Note For each scenario above, we recommend you use a temporary directory to avoid uploading incomplete files or reports. So your workflow should be: * create a temporary directory inside the `<output_root>/<authorization_uuid>`, such as `<output_root>/<authorization_uuid>/tmp_reports/`   * place your result file(s) in the `tmp_reports` directory (as in the above table) * rename the directory from `tmp_reports` to `reports`  We recommend running the Toolkit in a cronjob, wrapped by some locking mechanism. Also, Toolkit logs are very minimal but can be very helpful when debugging an issue, so please consider saving them to a file. For example, the following cronjob runs the Toolkit every minute:  ```bash # Open the crontab crontab -e ```  PHP Toolkit  ```bash # Add the following line (replace <lumminary-toolkit-directory> with the absolute path of the Lumminary Toolkit) * * * * * flock /var/lock/lumminary-toolkit.lock php <lumminary-toolkit-directory>/lumminary-partner-toolkit.php --config-path <lumminary-toolkit-directory>/config/my-product1-config.json >> /var/log/lumminary-toolkit.log ```  Python Toolkit  ```bash # Add the following line (replace <lumminary-toolkit-directory> with the absolute path of the Lumminary Toolkit) * * * * * flock /var/lock/lumminary-toolkit.lock source env/bin/activate; python <lumminary-toolkit-directory>/lumminary_partner_toolkit.py --config-path <lumminary-toolkit-directory>/config/my-product1-config.json ```  ## API endpoints Lumminary provides two endpoint APIs, sandbox and production. You can use the sandbox for your integration and testing, simulate orders, upload genetic data, and generate reports. The sandbox works exactly like the production environment, and you can test your end-to-end integration.  In order to simulate a complete order, you need to use this test credit card:   |Credit card number  | Expiration date| CVV2| |--------------------|----------------|-----| |4242 4242 4242 4242 |  12/30         | 123 |  ### Sandbox website: [sandbox-www.lumminary.com](https://sandbox-www.lumminary.com)  api-hostname: [sandbox-api.lumminary.com/v1](https://sandbox-api.lumminary.com/v1)  ### Production website: [lumminary.com](https://lummianary.com)  api-hostname: [api.lumminary.com/v1](https://api.lumminary.com/v1)  # Obtaining credentials To obtain credentials, you need to register as a Lumminary partner. You can do this by [filling in this form](https://lumminary.com/register-for-connect-with-lumminary).  You will then receive the following:  |Credentials|Description| |-------|-------| |Product UUID|Each product you register on the Lumminary platform gets an UUID which will be used to identify that product to the Lumminary API| |API key|The secret API key associated with the Product UUID| |Partner UUID|Upon your first registration on the Lumminary platform, you will receive a single Partner UUID, which identifies you as one entity, regardless of product. This identifier is used for the Connect with Lumminary (CWL) functionality.| |CWL Encryption Key|The CWL encryption key is associated with the Partner UUID and is used to encrypt all communication for the Connect with Lumminary functionality.|  Each product or service needs to have its own product UUID and API key, which means you have to fill in the form for all products and services that require access to Lumminary customer data.    ## Configure the credentials to the Lumminary API Client The easiest way to set up your credentials is to use an environment file.  For this, you must create a file named `env.json` (but any name will do) in your project directory, which should contain: ```json {     \"product_uuid\": <your_product_uuid>,     \"api_key\": <your_product_api_key>,     \"role\": \"role_product\",     \"api_host\": <lumminary_api_hostname_endpoint> } ```  In order to load the Credentials from the `env.json`, you can use the following code:  #### PHP example: ```php require_once(__DIR__.\"/vendor/autoload.php\"); $credentials = new Lumminary\\Client\\Credentials(); $credentials->loadJSONCredentials(__DIR__.\"/env.json\"); ```  #### Python example: ```python import lumminary_sdk as lumminary import os  credentials = lumminary.Credentials() credentials.load_json_credentials(     os.path.join(         os.getcwd(),         \"env.json\"     ) ) ```  ## Alternative credentials configuration You also have the option of passing the credentials as constructor parameters when instantiating the `Credentials` class.  #### PHP example:  ```php require_once(__DIR__.\"/vendor/autoload.php\"); $credentials = new Lumminary\\Client\\Credentials(     <lumminary_api_hostname_endpoint>,     <your_product_uuid>,     <your_product_api_key> ); ```  #### Python example:  ```python import lumminary_sdk as lumminary  credentials = lumminary.Credentials(     product_uuid = <your_product_uuid>,     api_key = <your_product_api_key>,     api_host = <lumminary_api_hostname_endpoint>,     role = \"role_product\" ) ```  ## Create an API instance  With the credentials configured and loaded, you can create an API client like so :   #### PHP example  ```php $apiClient = new Lumminary\\Client\\ApiClient($credentials); ```  #### Python example  ```python apiClient = lumminary.LumminaryApi(credentials) ```  # Query customers authorizations An Authorization represents permission from a client to access their personal and genetic data.   There are 2 situations where customers grant you access to their data:  * when a customer buys your product from the Lumminary DNA App Store * when a customer clicks on the \"Connect with Lumminary\" button on your website  Each time either of the above situations happens, our platform creates an Authorization UUID. You can reliably assume that if you have an Authorization UUID, you automatically have access to all the personal information and genetic data needed by your products and services. After you process an Authorization you need to mark it as processed; processed Authorizations will no longer be on the list of new authorizations.  There are two ways to obtain the Authorization UUID: * _polling_ - this method allows you to periodically interrogate our API and pulls the list of Authorization UUIDs.  * _webhooks_ (coming soon) - this method allows our API to push the Authorization UUIDs into your platform.  ## Poll method  To use the polling method, your servers periodically interrogate for new Authorization UUIDs. Please keep in mind that Authorizations not marked as processed will always be returned when polling for new Authorizations. This means there's a risk of parallel processing the same Authorization. To avoid this, you can, for example, consider using locking when processing.  #### A PHP example of using the polling API looks like:  ```php $productAuthorizations = $apiClient->getAuthorizationsQueue(     $apiClient->getCredentials()->getProductUuid(), );  foreach($productAuthorizations as $productAuthorization) {     /_**      *  Add your code for processing customer data here      **_/           // Mark Authorization as processed      $apiClient->postProductAuthorization(         $productAuthorization[\"productUuid\"],         $productAuthorization[\"authorizationUuid\"]     ); } ```  #### A Python example of using the polling API looks like:  ```python productAuthorizations = apiClient.get_authorizations_queue(     apiClient.get_credentials().product_uuid )  for productAuthorization in productAuthorizations:     #######     #   Add your code for processing customer data here     #######      # Mark Authorization as processed     apiClient.post_product_authorization(         productAuthorization.product_uuid,         productAuthorization.authorization_uuid     ) ```  Based on the Authorization object obtained previously, we can now query the customer's information (personal details and genetic data).  #### PHP example: ```php $authorizationMetadata = $apiClient->authorizationMetadata($productAuthorization[\"authorizationUuid\"]); ```  #### Python example: ```python authorizationMetadata = apiClient.authorization_metadata(productAuthorization.authorization_uuid) ```  #### authorizationMetadata object object structure  | Attribute name            | Description                                                                                | |:-------------------------:|:-------------------------------------------------------------------------------------------| | `customer`                | The UUID of the customer granting the Authorization                                        | | `product`                 | The UUID of the product that was authorized (your product UUID)                            | | `authorization`           | The UUID of the granted Authorization.                                                     | | `created_timestamp_utc`   | The unix timestamp in UTC time zone when the customer granted the Authorization            | | `dataset`                 | (present only if requested) The UUID of the dataset authorized by the customer             | | `customer_email`          | (present only if requested) Customer contact email                                         | | `customer_name`           | (present only if requested) Customer name                                                  | | `customer_address`        | (present only if requested) Customer address                                               |  By *present only if requested* we mean this attribute will be returned if at the time of configuring either the \"Connect with Lumminary\" button or your product, you have explicitly requested for that particular set of data.  # Query customer genetic data Based on the Authorization object obtained previously, now we have authorizationMetadata which contains the customer's information (personal details and genetic data). Let's use this information to extract some customer genetic data.  ## Get individual SNPs Out of all the available SNPs in the dataset, you can only access those for which the customer has previously granted permission.  For example, fetching details for a particular SNP:  #### PHP example: ```php $rsId = \"rs114326054\"; $snpDetails = null;  // check to see if you have access to the customer genetic data if (isset($productAuthorization[\"scopes\"][\"dataset\"])) {     // get SNP information     $snpDetails = $apiClient->getClientSnp(         $productAuthorization[\"clientUuid\"],         $productAuthorization[\"scopes\"][\"dataset\"],         $rsId     ); } ```  #### Python example: ```python rsId = \"rs114326054\" snpDetails = None  # check to see if you have access to the customer genetic data if hasattr(productAuthorization.scopes, \"dataset\"):     # get SNP information     snpDetails = apiClient.get_client_snp(         productAuthorization.client_uuid,         productAuthorization.scopes.dataset,         rsId     ) ```  ##### The snpDetails object will contain these important attributes:  | Attribute name PHP     | Attribute name Python        | Description                                               | |:-------------------------:|:-------------------------:|:----------------------------------------------------------| | `snpId`                 | `snp_id`                    | The rsid of the SNP                                       | | `referenceGenome`        |`reference_genome`          | The reference genome known to be used by the Dataset's source. <br> This impacts the reference allele, location, and based on the dbSNP build, also the SNP's accession | | `genotypedAlleles`       | `genotyped_alleles`        | The genotype value of the customer's queried SNP. <br><br> If the attribute of this SNP has the `phased` flag set to True, <br>the first items in the lists for all SNPs will be on the same inherited chromosome, <br>and analogous for the second item. <br><br> If the SNP is unphased, the order of the items is irrelevant | |`phased`                   | `phased`                  | A boolean. True if the SNP is known to be phased, False otherwise | |`chromosomeAccession`     | `chromosome_accession`     | This is the chromosome accession number where the SNP is located; in the format of NC_00x | |`location`                 | `location`                | This is the customer's SNP's location on the chromosome |  When trying to access any customer's SNP for which you don't have permission, an `Unauthorized` exception will be raised.  ## Get all authorized SNPs  The function below returns all SNPs your product has access to. These are all the SNPs configured as mandatory for your product, as well as all SNPs that are configured as optional and available in the customer's data set. We encourage you to use this option if you need to get all available SNPs, because it is faster than fetching SNP details one by one.  For example, fetching all authorized SNPs:  #### PHP example: ```php $datasetSnps = null;  // check to see if you have access to the customer genetic data if (isset($productAuthorization[\"scopes\"][\"dataset\"])) {     // get all authorized SNPs     $datasetSnps = $apiClient->getClientSnpGroup(         $productAuthorization[\"clientUuid\"],          $productAuthorization[\"scopes\"][\"dataset\"]     ); } ```  #### Python example: ```python datasetSnps = None  # check to see if you have access to the customer genetic data if hasattr(productAuthorization.scopes, \"dataset\"):     # get all authorized SNPs     datasetSnps = apiClient.get_client_snp_group(         productAuthorization.client_uuid,         productAuthorization.scopes.dataset     ) ```  ##### The datasetSnps variable will be a list of objects each having the following attributes:  | Attribute name PHP     | Attribute name Python        | Description                                               | |:-------------------------:|:-------------------------:|:----------------------------------------------------------| | `snpId`                  | `snp_id`                   | The rsid of the SNP                                       | | `referenceGenome`        |`reference_genome`          | The reference genome known to be used by the Dataset's source. <br> This impacts the reference allele, location, and based on the dbSNP build, also the SNP's accession | | `genotypedAlleles`       | `genotyped_alleles`        | The genotype value of the customer's queried SNP. <br><br> If the attribute of this SNP has the `phased` flag set to True, <br>the first items in the lists for all SNPs will be on the same inherited chromosome, <br>and analogous for the second item. <br><br> If the SNP is unphased, the order of the items is irrelevant | |`phased`                   | `phased`                  | A boolean. True if the SNP is known to be phased, False otherwise | |`chromosomeAccession`     | `chromosome_accession`     | This is the chromosome accession number where the SNP is located; in the format of NC_00x | |`location`                 | `location`                | This is the customer's SNP's location on the chromosome |  When trying to access any customer's SNP for which you don't have permission, an `Unauthorized` exception will be raised.  ## Get Genes  Along with individual SNPs, you can also get all the authorized SNPs from a particular gene, that are available in the customer's dataset.  Here, by genes, we refer strictly to the genomic region that produces some protein, without considering regulatory or noncoding regions that influence gene expression.  The gene name (known as symbol) can be from either of these two databases - NCBI and Ensembl.  For example, fetching details for a gene symbol:  #### PHP example ```php $geneSymbol = \"C1ORF159\"; $geneDetails = null; // check to see if you have access to the customer genetic data if (isset($productAuthorization[\"scopes\"][\"dataset\"])) {     // get all authorized SNPs within a gene     $geneDetails = $apiClient->getClientGene(         $productAuthorization[\"clientUuid\"],         $productAuthorization[\"scopes\"][\"dataset\"],         $geneSymbol     ); } ```  #### Python example ```python geneSymbol = \"C1ORF159\" geneDetails = None # check to see if you have access to the customer genetic data if hasattr(productAuthorization.scopes, \"dataset\"):     # get all authorized SNPs within a gene     geneDetails = apiClient.get_client_gene(         productAuthorization.client_uuid,         productAuthorization.scopes.dataset,         geneSymbol     ) ```  ##### All the geneDetails object attributes are  | Attribute name PHP | Attribute name Python    | Description                                                                              | |:---------------------:|:---------------------:|:-----------------------------------------------------------------------------------------| | `molecularLocation`  | `molecular_location`   | An object containing the location of the gene within the chromosome - see below the molecular location object structure  | | `snps`                | `snps`                | A list of SNP objects present in the gene - see below the SNP object structure           | | `symbol`              | `symbol`              | The gene's accession string (name)                                                       |  ##### Molecular location attributes   | Attribute name PHP     | Attribute name Python    | Description                                                                              | |:-------------------------:|:---------------------:|:-----------------------------------------------------------------------------------------| | `chromosomeAccession`    | `chromosome_accession` | The scaffold/chromosome on which the gene is placed                                      | | `start`                   | `start`               | The gene's start position on the scaffold                                                | | `stop`                    | `stop`                | The gene's stop position on the scaffold                                                 |  ##### SNP object structure  | Attribute name PHP     | Attribute name Python    | Description                                                                              | |:-------------------------:|:---------------------:|:-----------------------------------------------------------------------------------------| | `referenceGenome`        | `reference_genome`     | The reference genome known to be used by the Dataset's source. <br> This impacts the reference allele, location, and based on the dbSNP build, also the SNP's accession| | `genotypedAlleles`       | `genotyped_alleles`    | The genotype value of the customer's queried SNP. <br><br> If the attribute of this SNP has the `phased` flag set to True, <br>the first items in the lists for all SNPs will be on the same inherited chromosome, <br>and analogous for the second item. <br><br> If the SNP is unphased, the order of the items is irrelevant                                          | | `phased`                  | `phased`              | A boolean. True if the SNP is known to be phased, False otherwise                         | | `chromosomeAccession`    | `chromosome_accession` | This is the chromosome accession number where the SNP is located; in the format of NC_00x | | `location`                | `location`            | This is the customer's SNP's location on the chromosome                                   |  ## Get customer genetic data in 23andMe tsv format  If your platform is already compatible with 23andMe genotype data files, you can use this specific function to generate data in the 23andMe format - list of rows in tab separated values.  #### PHP example: ```PHP $authorizationDnaData = $apiClient->authorizationDnaData($productAuthorization[\"authorizationUuid\"]); ```  #### Python example ```python authorizationDnaData = apiClient.authorization_dna_data(productAuthorization.authorization_uuid) ```  `authorizationDnaData` contains a list of rows in a tsv (tab delimited values)/csv format (23andme-compatible)  # Submit reports  After you finish analysing the customer's genetic data, we need to inform the customer their analysis is complete. To do this, you will notify us using the function below. Finally, the customer will then:  * access their report file through a written electronic document (eg. .pdf or .doc) * access their report on your website under an account with a username and a password or * receive a physical product  ## How to submit a report file  When you submit such a report file, Lumminary will save this document into the customer's account, from which the customer will then be able to access it directly.  #### PHP example ```php $pathToReportFile = <path_to_report_file>; $fileReport = new \\SplFileObject($pathToReportFile);  $friendlyFileName = \"report_file_name\"; //optional, give a friendly name to your report file $apiClient->postAuthorizationResultFile(    $productAuthorization[\"productUuid\"],    $productAuthorization[\"authorizationUuid\"],    $fileReport,    $friendlyFileName ); ```  #### Python example ```python pathToReport = <path_to_report_file> originalFilename = \"report_file_name\" #optional, give a friendly name to your report file apiClient.post_authorization_result_file(    productAuthorization.product_uuid,    productAuthorization.authorization_uuid,    pathToReport,    originalFilename ) ```  If you need to upload multiple files, you have to call the function for each file, one at a time.   ## How to submit a report so the customer can access it on your website  If the customer's results can be accessed on your website, you will need to create a customer account on your platform, generating a user and password which will be sent through the Lumminary API into the customer's Lumminary account.   In case you don't generate a user and a password for the customer to access their report, use the function below with \"null\" value to username and password. We recommend you use the URL for customer reports on a dedicated page for reports only, rather than your homepage or some other generic page.  #### PHP example: ```php $apiClient->postAuthorizationResultCredentials(    $productAuthorization[\"productUuid\"],    $productAuthorization[\"authorizationUuid\"],    <username_generated_by_you>, //optional, default null    <password_generated_by_you>, //optional, default null    <report_on_your_website_url> // https://partnerwebsite.com/reports.php?reportid=a7508 ); ```  #### Python example: ```python apiClient.post_authorization_result_credentials(    productAuthorization.product_uuid,    productAuthorization.authorization_uuid,    <username_generated_by_you>, # optional, default null    <password_generated_by_you>, # optional, default null    <report_on_your_website_url> # https://partnerwebsite.com/reports.php?reportid=a7508 ) ```  ## How to submit a physical product In case you only send the customer a physical product and you don't generate any reports, you need to run the function below so we can mark the order as fulfilled and can inform the client.  #### PHP example: ```php $apiClient->postProductAuthorization(   $productAuthorization[\"productUuid\"],   $productAuthorization[\"authorizationUuid\"] ); ```  #### Python example: ```python apiClient.post_product_authorization(    productAuthorization.product_uuid,    productAuthorization.authorization_uuid ) ```  # The Connect with Lumminary button  The \"Connect with Lumminary\" functionality allows you to get customer details and genetic data from the Lumminary platform for free, anytime you want, for as long the customer grants you access. This functionality offers your customers the option to share their genetic data and other personal information (e.g. name, address, email etc.) stored on the Lumminary platform.   Having this button on your website makes it very easy for the customer to share their genetic data with you, as they don't have to download and re-upload their data on your site. The customer always has the option to revoke your access to both their personal details and their genetic data.  **`To protect the customer's privacy, you are not allowed to save their data anywhere. You can, however, always access their data on the Lumminary platform, for as long as they grant you access. If you generate a report based on customer data, you are allowed to save that report on your platform.`**  In order to implement this functionality on your website, this is what you need to know: * Register your product on the Lumminary platform * Add the \"Connect with Lumminary\" button to your website * Configure your website to retrieve customer data * Possible errors  ## Register your product on the Lumminary platform  If you're new to the Lumminary platform and don't already have any products in the DNA App Store, then you need to register by [filling in this form](https://lumminary.com/register-for-connect-with-lumminary).  You have to fill in the form for all products and services that require access to Lumminary customers' genetic data.    ## Add the Connect with Lumminary button to your website  Since the CWL flow involves encrypting and decrypting data, we recommend installing the Lumminary API Client, where you'll find some specific helper functions.   In order to enable the button, you have to include the following script in the `<head>` tag of all the pages where you want to enable the “Connect with Lumminary” button:  ```html <head>     <script defer src=\"https://lumminary.com/cwl/cwl.js\"></script> </head> ```  The Javascript creates a CSRF token and attaches it to the button to be transmitted and verified on our servers each time a user clicks on the button. The CSRF token expires after 5 minutes. In case the CSRF token is expired or tampered, the user will be redirected to your website where it's up to you to decide what to do next - reload the page with the button or show the customer an error message.  The `cwl.js` file is loaded as a deferred resource, which means that it will load after all the webpage code execution has been finished, so it will not have any impact on your website load speed.  ### Chose a button colour  There are two type of buttons, so you can pick one that matches your branding. The buttons are SVG images, which means that you can scale them up or down to fit your design, without compromising on image quality. You can do this by changing the image height.  ##### a. White button version   <img src=\"https://lumminary.com/cwl/connect-with-lumminary-white.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/>  <br>  ```html <a class=\"lumminary-connect-btn\" data-partner-uuid=\"<partner-UUID>\" data-request=\"<request>\" style=\"cursor:pointer; text-decoration:none;\" href=\"https://lumminary.com\">    <img src=\"https://lumminary.com/cwl/connect-with-lumminary-white.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/> </a> ```  ##### b.  Black button version  <img src=\"https://lumminary.com/cwl/connect-with-lumminary-black.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/>  <br>  ```html <a class=\"lumminary-connect-btn\" data-partner-uuid=\"<partner-UUID>\" data-request=\"<request>\" style=\"cursor:pointer; text-decoration:none;\" href=\"https://lumminary.com\">    <img src=\"https://lumminary.com/cwl/connect-with-lumminary-black.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"/> </a> ```  ## Button configuration  Each button has 2 attributes which need to be configured:  1. **data-partner-uuid** where you have to add your partner UUID (you have received the partner UUID after filling in the form for product registration).  2. **data-request** which is a string obtained by encrypting a serialized JSON (you have received the CWL encryption key after filling in the form for product registration). See details below.   #### Data-request object  The data-request object has a standard format which needs to be preserved. It is formed of two types of data, some mandatory and some optional. You can use the optional fields to add any metadata or other information for your own use. The data-request object is going to be returned with the response from the authentication without being altered.  ##### Mandatory information  The mandatory information is a list of scopes which you ask the client to grant permission for. These scopes are comma delimited, and the possible options are: `address`, `email`, `dataset`.  The scopes _address_, _email_, and _dataset_ can be used in any combination; you must request at least one scope.  | Attribute name    | Description                                         | |:-----------------:|:----------------------------------------------------| | `address`         | Requests access to a customer's name and address.   | | `email`           | Requests access to a customer's email address.      | | `dataset`         | Requests access to a customer's genetic data        |  #### PHP example: ```php $objAuthorizationRequest [\"scopes\"] = \"address,dataset,email\"; ```  #### Python example: ```python objAuthorizationRequest [\"scopes\"] = \"address,dataset,email\" ```  Product UUID is your `productUuid` for which you ask customer permissions.  #### PHP example: ```php $objAuthorizationRequest[\"productUuid\"] = $credentials->getProductUuid(); ```  #### Python example: ```python objAuthorizationRequest[\"productUuid\"] = credentials.product_uuid ```  ##### Optional information  In the optional part of the object, you can add any useful data, such as customer ID,  session ID, or any parameter which can help you identify the response from Lumminary.  #### PHP example: ```php $objAuthorizationRequest[\"customData\"] = array(); $objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id>; $objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session>; $objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data>; ```  #### Python example: ```python objAuthorizationRequest[\"customData\"] = {} objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id> objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session> objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data> ```  See below a complete example for a data-request object:  #### PHP example: ```php $objAuthorizationRequest[\"scopes\"] = \"address,dataset,email\"; $objAuthorizationRequest[\"productUuid\"] = <product-UUID>;  $objAuthorizationRequest[\"customData\"] = array(); $objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id>; $objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session>; $objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data>; ```  #### Python example: ```python objAuthorizationRequest = {} objAuthorizationRequest[\"scopes\"] = \"address,dataset,email\" objAuthorizationRequest[\"productUuid\"] = <product-UUID>  objAuthorizationRequest[\"customData\"] = {} objAuthorizationRequest[\"customData\"][\"customerId\"] = <partner-customer-id> objAuthorizationRequest[\"customData\"][\"websiteSession\"] = <customer-session> objAuthorizationRequest[\"customData\"][\"customData3\"] = <Some addional data> ```  ## Creating the Authorization Request  The previously generated object (`objAuthorizationRequest`) will now need to be encrypted. In order to be able to encrypt the object and also query the Lumminary API to obtain the customer details and genetic data, you need to have the Lumminary API Client installed. If you haven't done this already, please follow these [steps](#Install-Lumminary-API-Client-andor-Toolkit).  ### Add data-request attribute  After you have the Lumminary API Client installed correctly you can use the command below:  #### PHP example: ```php // You have recieved the CWL encryption key after filling in the form for product registration $partnerCwlKey = <partner-encryption-key>; $requestValueEncryptedUrlEncoded = Lumminary\\Client\\LumminaryApi::cwl_data_request_build(     $objAuthorizationRequest,     $partnerCwlKey ); ```  #### Python example: ```python import lumminary_sdk as lumminary  # You have recieved the CWL encryption key after filling in the form for product partnerCwlKey = <partner-encryption-key>  requestValueEncryptedUrlEncoded = lumminary.LumminaryApi.cwl_data_request_build(objAuthorizationRequest, partnerCwlKey) ```  The resulting string should be added in the `data-request` attribute of the `<a>` tag of the \"Connect with Lumminary\" button.  ### Add data-partner-uuid attribute  Add the `data-partner-uuid` in the `data-partner-uuid` attribute of the `<a>` tag of the \"Connect with Lumminary\" button. You have received the partner UUID after filling in the form for product registration.  An example of a button correctly configured should look like this:  ```html <a class=\"lumminary-connect-btn\" data-partner-uuid=\"4231-7446-2543-6542\" data-request=\"7LfMX811Als0l%2FAvf84pB7n3mcycnTjgWl1FaVNffdqiOApMn4HAnk0Ux6eatObfYmxf1xPRjo7nBojsL4ImgOL932NK2Ei4VoUXjs9Y%2BcvphI0kxBSblLaeVXNPbJO9LsuNP%2BHJzDBAnZZdAObgYxHH2QDY3VD%2Ff%2FBXKw9WYDdBssAoegMFEJ9GgYutFQ4nTPXAt%2FdWCqoxYbZrYpCj2Pphk9lstc4Ib%2BLNxKiEtNCmVGr6sgmR2lPBwgylTsEX%2FMRCJb6sdQyZBhvSQCMFb0p3%2B9tEwV0%3D\" style=\"cursor:pointer; text-decoration:none;\" href=\"https://lumminary.com\">    <img src=\"https://lumminary.com/cwl/connect-with-lumminary-white.svg\" alt=\"Lumminary DNA tests\" height=\"50\" title=\"Connect with Lumminary\"> </a> ```  ## Connect with Lumminary summary of user interaction  When a customer clicks on the “Connect with Lumminary” button, a pop-up window opens. After they choose which genetic file to share, the pop-up will automatically close and the user will be redirected to your callback URL in the parent window. Your callback URL needs to be predefined in the Lumminary partner portal.   The GET request from the client to your callback URL will contain two querystring parameters - `request` and `response`:  1. `request` – this is exactly the same request that you previously sent in the `data-request` field. You can decrypt it with the CWL encryption key which you used to encrypt it. 2. `response` – the response is an urlencoded encrypted serialized JSON object which contains the Authorization UUID and the Authorization UTC unix timestamp. You will use the Authorization UUID to get the customer's data with the Lumminary API Client. The response string is encrypted with your CWL encryption key, the same as the `data-request` parameter.   In order to decrypt the `response` parameter, you can use the following function:  #### PHP example: ```php // the entire callback URL, including the querystring parameters $callbackUrlWithPayload = \"https://partnerwebsite.con/callback?request=...&response=...\";  $cwlReturnObject = Lumminary\\Client\\LumminaryApi::cwl_url_query_extract(     $callbackUrlWithPayload,      $partnerCwlKey   ); ```  #### Python example: ```python // the entire callback URL, including the querystring parameters callback_url_with_payload = \"https://partnerwebsite.con/callback?request=...&response=...\"  cwlReturnObject = apiClient.cwl_url_query_extract(     callback_url_with_payload,     partner_cwl_key ) ```  The `cwlReturnObject` will now contain an object like the example below:  ```json {     \"request\": <your-request-parameter-echoed>,     \"response\": {         \"authorizationUuid\": <cwl-authorization-uuid>,         \"authorizationTimestamp\": <cwl-authorization-created-timestamp>     } } ```  With the Authorization UUID (`authorizationUuid`) you can [query all the customer details](#Query-customer-genetic-data) from the Lumminary platform.  ## Possible errors  When an error occurs, the customer is redirected to your callback URL. The redirect contains two querystring parameters - `request` and `response` - exactly like a regular response, but the `response` parameter contains an error object (see below) instead of an Authorization object.  #### PHP example: ```php // the entire callback url, including the querystring parameters $callbackUrlWithPayload = \"https://partnerwebsite.con/callback?request=...&response=...\";  $cwlReturnObject = Lumminary\\Client\\LumminaryApi::cwl_url_query_extract(     $callbackUrlWithPayload,      $partnerCwlKey   ); ```  #### Python example: ```python # the entire callback url, including the querystring parameters callback_url_with_payload = \"https://partnerwebsite.con/callback?request=...&response=...\"  cwlReturnObject = apiClient.cwl_url_query_extract(     callback_url_with_payload,     partner_cwl_key ) ```  Example of a return object (`cwlReturnObject`) containing an error message:  ```json {     \"request\": <your-request-parameter-echoed>,     \"response\": {         \"error\": {             \"id\": <error id>,             \"message\": <error message>         }     } } ```  | Error Id          | Error Message                                                                                | |:-----------------:|:---------------------------------------------------------------------------------------------| | 1                 | Invalid Security Token                                                                       | | 2                 | Invalid Access Scopes                                                                        | | 3                 | Customer refuses your request (this happens when the customer cancels instead of granting access) |
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import okhttp3.*;
import okhttp3.internal.http.HttpMethod;
import okhttp3.internal.tls.OkHostnameVerifier;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import okio.Buffer;
import okio.BufferedSink;
import okio.Okio;

import javax.net.ssl.*;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.Type;
import java.net.URI;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import java.security.KeyStore;
import java.security.SecureRandom;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.text.DateFormat;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.openapitools.client.auth.Authentication;
import org.openapitools.client.auth.HttpBasicAuth;
import org.openapitools.client.auth.HttpBearerAuth;
import org.openapitools.client.auth.ApiKeyAuth;

/**
 * <p>ApiClient class.</p>
 */
public class ApiClient {

    private String basePath = "http://api.lumminary.com/v1";
    protected List<ServerConfiguration> servers = new ArrayList<ServerConfiguration>(Arrays.asList(
    new ServerConfiguration(
      "//api.lumminary.com/v1",
      "No description provided",
      new HashMap<String, ServerVariable>()
    )
  ));
    protected Integer serverIndex = 0;
    protected Map<String, String> serverVariables = null;
    private boolean debugging = false;
    private Map<String, String> defaultHeaderMap = new HashMap<String, String>();
    private Map<String, String> defaultCookieMap = new HashMap<String, String>();
    private String tempFolderPath = null;

    private Map<String, Authentication> authentications;

    private DateFormat dateFormat;
    private DateFormat datetimeFormat;
    private boolean lenientDatetimeFormat;
    private int dateLength;

    private InputStream sslCaCert;
    private boolean verifyingSsl;
    private KeyManager[] keyManagers;

    private OkHttpClient httpClient;
    private JSON json;

    private HttpLoggingInterceptor loggingInterceptor;

    /**
     * Basic constructor for ApiClient
     */
    public ApiClient() {
        init();
        initHttpClient();

        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("Bearer", new ApiKeyAuth("header", "Authorization"));
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    /**
     * Basic constructor with custom OkHttpClient
     *
     * @param client a {@link okhttp3.OkHttpClient} object
     */
    public ApiClient(OkHttpClient client) {
        init();

        httpClient = client;

        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("Bearer", new ApiKeyAuth("header", "Authorization"));
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    private void initHttpClient() {
        initHttpClient(Collections.<Interceptor>emptyList());
    }

    private void initHttpClient(List<Interceptor> interceptors) {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        builder.addNetworkInterceptor(getProgressInterceptor());
        for (Interceptor interceptor: interceptors) {
            builder.addInterceptor(interceptor);
        }

        httpClient = builder.build();
    }

    private void init() {
        verifyingSsl = true;

        json = new JSON();

        // Set default User-Agent.
        setUserAgent("OpenAPI-Generator/1.0/java");

        authentications = new HashMap<String, Authentication>();
    }

    /**
     * Get base path
     *
     * @return Base path
     */
    public String getBasePath() {
        return basePath;
    }

    /**
     * Set base path
     *
     * @param basePath Base path of the URL (e.g http://api.lumminary.com/v1
     * @return An instance of OkHttpClient
     */
    public ApiClient setBasePath(String basePath) {
        this.basePath = basePath;
        this.serverIndex = null;
        return this;
    }

    public List<ServerConfiguration> getServers() {
        return servers;
    }

    public ApiClient setServers(List<ServerConfiguration> servers) {
        this.servers = servers;
        return this;
    }

    public Integer getServerIndex() {
        return serverIndex;
    }

    public ApiClient setServerIndex(Integer serverIndex) {
        this.serverIndex = serverIndex;
        return this;
    }

    public Map<String, String> getServerVariables() {
        return serverVariables;
    }

    public ApiClient setServerVariables(Map<String, String> serverVariables) {
        this.serverVariables = serverVariables;
        return this;
    }

    /**
     * Get HTTP client
     *
     * @return An instance of OkHttpClient
     */
    public OkHttpClient getHttpClient() {
        return httpClient;
    }

    /**
     * Set HTTP client, which must never be null.
     *
     * @param newHttpClient An instance of OkHttpClient
     * @return Api Client
     * @throws java.lang.NullPointerException when newHttpClient is null
     */
    public ApiClient setHttpClient(OkHttpClient newHttpClient) {
        this.httpClient = Objects.requireNonNull(newHttpClient, "HttpClient must not be null!");
        return this;
    }

    /**
     * Get JSON
     *
     * @return JSON object
     */
    public JSON getJSON() {
        return json;
    }

    /**
     * Set JSON
     *
     * @param json JSON object
     * @return Api client
     */
    public ApiClient setJSON(JSON json) {
        this.json = json;
        return this;
    }

    /**
     * True if isVerifyingSsl flag is on
     *
     * @return True if isVerifySsl flag is on
     */
    public boolean isVerifyingSsl() {
        return verifyingSsl;
    }

    /**
     * Configure whether to verify certificate and hostname when making https requests.
     * Default to true.
     * NOTE: Do NOT set to false in production code, otherwise you would face multiple types of cryptographic attacks.
     *
     * @param verifyingSsl True to verify TLS/SSL connection
     * @return ApiClient
     */
    public ApiClient setVerifyingSsl(boolean verifyingSsl) {
        this.verifyingSsl = verifyingSsl;
        applySslSettings();
        return this;
    }

    /**
     * Get SSL CA cert.
     *
     * @return Input stream to the SSL CA cert
     */
    public InputStream getSslCaCert() {
        return sslCaCert;
    }

    /**
     * Configure the CA certificate to be trusted when making https requests.
     * Use null to reset to default.
     *
     * @param sslCaCert input stream for SSL CA cert
     * @return ApiClient
     */
    public ApiClient setSslCaCert(InputStream sslCaCert) {
        this.sslCaCert = sslCaCert;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>keyManagers</code>.</p>
     *
     * @return an array of {@link javax.net.ssl.KeyManager} objects
     */
    public KeyManager[] getKeyManagers() {
        return keyManagers;
    }

    /**
     * Configure client keys to use for authorization in an SSL session.
     * Use null to reset to default.
     *
     * @param managers The KeyManagers to use
     * @return ApiClient
     */
    public ApiClient setKeyManagers(KeyManager[] managers) {
        this.keyManagers = managers;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>dateFormat</code>.</p>
     *
     * @return a {@link java.text.DateFormat} object
     */
    public DateFormat getDateFormat() {
        return dateFormat;
    }

    /**
     * <p>Setter for the field <code>dateFormat</code>.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setDateFormat(DateFormat dateFormat) {
        JSON.setDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set SqlDateFormat.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setSqlDateFormat(DateFormat dateFormat) {
        JSON.setSqlDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set OffsetDateTimeFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        JSON.setOffsetDateTimeFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LocalDateFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLocalDateFormat(DateTimeFormatter dateFormat) {
        JSON.setLocalDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LenientOnJson.</p>
     *
     * @param lenientOnJson a boolean
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLenientOnJson(boolean lenientOnJson) {
        JSON.setLenientOnJson(lenientOnJson);
        return this;
    }

    /**
     * Get authentications (key: authentication name, value: authentication).
     *
     * @return Map of authentication objects
     */
    public Map<String, Authentication> getAuthentications() {
        return authentications;
    }

    /**
     * Get authentication for the given name.
     *
     * @param authName The authentication name
     * @return The authentication, null if not found
     */
    public Authentication getAuthentication(String authName) {
        return authentications.get(authName);
    }


    /**
     * Helper method to set username for the first HTTP basic authentication.
     *
     * @param username Username
     */
    public void setUsername(String username) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setUsername(username);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set password for the first HTTP basic authentication.
     *
     * @param password Password
     */
    public void setPassword(String password) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setPassword(password);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set API key value for the first API key authentication.
     *
     * @param apiKey API key
     */
    public void setApiKey(String apiKey) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKey(apiKey);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set API key prefix for the first API key authentication.
     *
     * @param apiKeyPrefix API key prefix
     */
    public void setApiKeyPrefix(String apiKeyPrefix) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKeyPrefix(apiKeyPrefix);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set access token for the first OAuth2 authentication.
     *
     * @param accessToken Access token
     */
    public void setAccessToken(String accessToken) {
        throw new RuntimeException("No OAuth2 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param sessionToken Session Token
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String sessionToken, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Set the User-Agent header's value (by adding to the default header map).
     *
     * @param userAgent HTTP request's user agent
     * @return ApiClient
     */
    public ApiClient setUserAgent(String userAgent) {
        addDefaultHeader("User-Agent", userAgent);
        return this;
    }

    /**
     * Add a default header.
     *
     * @param key The header's key
     * @param value The header's value
     * @return ApiClient
     */
    public ApiClient addDefaultHeader(String key, String value) {
        defaultHeaderMap.put(key, value);
        return this;
    }

    /**
     * Add a default cookie.
     *
     * @param key The cookie's key
     * @param value The cookie's value
     * @return ApiClient
     */
    public ApiClient addDefaultCookie(String key, String value) {
        defaultCookieMap.put(key, value);
        return this;
    }

    /**
     * Check that whether debugging is enabled for this API client.
     *
     * @return True if debugging is enabled, false otherwise.
     */
    public boolean isDebugging() {
        return debugging;
    }

    /**
     * Enable/disable debugging for this API client.
     *
     * @param debugging To enable (true) or disable (false) debugging
     * @return ApiClient
     */
    public ApiClient setDebugging(boolean debugging) {
        if (debugging != this.debugging) {
            if (debugging) {
                loggingInterceptor = new HttpLoggingInterceptor();
                loggingInterceptor.setLevel(Level.BODY);
                httpClient = httpClient.newBuilder().addInterceptor(loggingInterceptor).build();
            } else {
                final OkHttpClient.Builder builder = httpClient.newBuilder();
                builder.interceptors().remove(loggingInterceptor);
                httpClient = builder.build();
                loggingInterceptor = null;
            }
        }
        this.debugging = debugging;
        return this;
    }

    /**
     * The path of temporary folder used to store downloaded files from endpoints
     * with file response. The default value is <code>null</code>, i.e. using
     * the system's default temporary folder.
     *
     * @see <a href="https://docs.oracle.com/javase/7/docs/api/java/nio/file/Files.html#createTempFile(java.lang.String,%20java.lang.String,%20java.nio.file.attribute.FileAttribute...)">createTempFile</a>
     * @return Temporary folder path
     */
    public String getTempFolderPath() {
        return tempFolderPath;
    }

    /**
     * Set the temporary folder path (for downloading files)
     *
     * @param tempFolderPath Temporary folder path
     * @return ApiClient
     */
    public ApiClient setTempFolderPath(String tempFolderPath) {
        this.tempFolderPath = tempFolderPath;
        return this;
    }

    /**
     * Get connection timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getConnectTimeout() {
        return httpClient.connectTimeoutMillis();
    }

    /**
     * Sets the connect timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param connectionTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setConnectTimeout(int connectionTimeout) {
        httpClient = httpClient.newBuilder().connectTimeout(connectionTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get read timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getReadTimeout() {
        return httpClient.readTimeoutMillis();
    }

    /**
     * Sets the read timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param readTimeout read timeout in milliseconds
     * @return Api client
     */
    public ApiClient setReadTimeout(int readTimeout) {
        httpClient = httpClient.newBuilder().readTimeout(readTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get write timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getWriteTimeout() {
        return httpClient.writeTimeoutMillis();
    }

    /**
     * Sets the write timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param writeTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setWriteTimeout(int writeTimeout) {
        httpClient = httpClient.newBuilder().writeTimeout(writeTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }


    /**
     * Format the given parameter object into string.
     *
     * @param param Parameter
     * @return String representation of the parameter
     */
    public String parameterToString(Object param) {
        if (param == null) {
            return "";
        } else if (param instanceof Date || param instanceof OffsetDateTime || param instanceof LocalDate) {
            //Serialize to json string and remove the " enclosing characters
            String jsonStr = JSON.serialize(param);
            return jsonStr.substring(1, jsonStr.length() - 1);
        } else if (param instanceof Collection) {
            StringBuilder b = new StringBuilder();
            for (Object o : (Collection) param) {
                if (b.length() > 0) {
                    b.append(",");
                }
                b.append(o);
            }
            return b.toString();
        } else {
            return String.valueOf(param);
        }
    }

    /**
     * Formats the specified query parameter to a list containing a single {@code Pair} object.
     *
     * Note that {@code value} must not be a collection.
     *
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list containing a single {@code Pair} object.
     */
    public List<Pair> parameterToPair(String name, Object value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value instanceof Collection) {
            return params;
        }

        params.add(new Pair(name, parameterToString(value)));
        return params;
    }

    /**
     * Formats the specified collection query parameters to a list of {@code Pair} objects.
     *
     * Note that the values of each of the returned Pair objects are percent-encoded.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list of {@code Pair} objects.
     */
    public List<Pair> parameterToPairs(String collectionFormat, String name, Collection value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value.isEmpty()) {
            return params;
        }

        // create the params based on the collection format
        if ("multi".equals(collectionFormat)) {
            for (Object item : value) {
                params.add(new Pair(name, escapeString(parameterToString(item))));
            }
            return params;
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        // escape all delimiters except commas, which are URI reserved
        // characters
        if ("ssv".equals(collectionFormat)) {
            delimiter = escapeString(" ");
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = escapeString("\t");
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = escapeString("|");
        }

        StringBuilder sb = new StringBuilder();
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(escapeString(parameterToString(item)));
        }

        params.add(new Pair(name, sb.substring(delimiter.length())));

        return params;
    }

    /**
    * Formats the specified free-form query parameters to a list of {@code Pair} objects.
    *
    * @param value The free-form query parameters.
    * @return A list of {@code Pair} objects.
    */
    public List<Pair> freeFormParameterToPairs(Object value) {
        List<Pair> params = new ArrayList<>();

        // preconditions
        if (value == null || !(value instanceof Map )) {
            return params;
        }

        final Map<String, Object> valuesMap = (Map<String, Object>) value;

        for (Map.Entry<String, Object> entry : valuesMap.entrySet()) {
            params.add(new Pair(entry.getKey(), parameterToString(entry.getValue())));
        }

        return params;
    }


    /**
     * Formats the specified collection path parameter to a string value.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param value The value of the parameter.
     * @return String representation of the parameter
     */
    public String collectionPathParameterToString(String collectionFormat, Collection value) {
        // create the value based on the collection format
        if ("multi".equals(collectionFormat)) {
            // not valid for path params
            return parameterToString(value);
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        if ("ssv".equals(collectionFormat)) {
            delimiter = " ";
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = "\t";
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = "|";
        }

        StringBuilder sb = new StringBuilder() ;
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(parameterToString(item));
        }

        return sb.substring(delimiter.length());
    }

    /**
     * Sanitize filename by removing path.
     * e.g. ../../sun.gif becomes sun.gif
     *
     * @param filename The filename to be sanitized
     * @return The sanitized filename
     */
    public String sanitizeFilename(String filename) {
        return filename.replaceAll(".*[/\\\\]", "");
    }

    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     *   application/json
     *   application/json; charset=UTF8
     *   APPLICATION/JSON
     *   application/vnd.company+json
     * "* / *" is also default to JSON
     * @param mime MIME (Multipurpose Internet Mail Extensions)
     * @return True if the given MIME is JSON, false otherwise.
     */
    public boolean isJsonMime(String mime) {
        String jsonMime = "(?i)^(application/json|[^;/ \t]+/[^;/ \t]+[+]json)[ \t]*(;.*)?$";
        return mime != null && (mime.matches(jsonMime) || mime.equals("*/*"));
    }

    /**
     * Select the Accept header's value from the given accepts array:
     *   if JSON exists in the given array, use it;
     *   otherwise use all of them (joining into a string)
     *
     * @param accepts The accepts array to select from
     * @return The Accept header to use. If the given array is empty,
     *   null will be returned (not to set the Accept header explicitly).
     */
    public String selectHeaderAccept(String[] accepts) {
        if (accepts.length == 0) {
            return null;
        }
        for (String accept : accepts) {
            if (isJsonMime(accept)) {
                return accept;
            }
        }
        return StringUtil.join(accepts, ",");
    }

    /**
     * Select the Content-Type header's value from the given array:
     *   if JSON exists in the given array, use it;
     *   otherwise use the first one of the array.
     *
     * @param contentTypes The Content-Type array to select from
     * @return The Content-Type header to use. If the given array is empty,
     *   returns null. If it matches "any", JSON will be used.
     */
    public String selectHeaderContentType(String[] contentTypes) {
        if (contentTypes.length == 0) {
            return null;
        }

        if (contentTypes[0].equals("*/*")) {
            return "application/json";
        }

        for (String contentType : contentTypes) {
            if (isJsonMime(contentType)) {
                return contentType;
            }
        }

        return contentTypes[0];
    }

    /**
     * Escape the given string to be used as URL query value.
     *
     * @param str String to be escaped
     * @return Escaped string
     */
    public String escapeString(String str) {
        try {
            return URLEncoder.encode(str, "utf8").replaceAll("\\+", "%20");
        } catch (UnsupportedEncodingException e) {
            return str;
        }
    }

    /**
     * Deserialize response body to Java object, according to the return type and
     * the Content-Type response header.
     *
     * @param <T> Type
     * @param response HTTP response
     * @param returnType The type of the Java object
     * @return The deserialized Java object
     * @throws org.openapitools.client.ApiException If fail to deserialize response body, i.e. cannot read response body
     *   or the Content-Type of the response is not supported.
     */
    @SuppressWarnings("unchecked")
    public <T> T deserialize(Response response, Type returnType) throws ApiException {
        if (response == null || returnType == null) {
            return null;
        }

        if ("byte[]".equals(returnType.toString())) {
            // Handle binary response (byte array).
            try {
                return (T) response.body().bytes();
            } catch (IOException e) {
                throw new ApiException(e);
            }
        } else if (returnType.equals(File.class)) {
            // Handle file downloading.
            return (T) downloadFileFromResponse(response);
        }

        String respBody;
        try {
            if (response.body() != null)
                respBody = response.body().string();
            else
                respBody = null;
        } catch (IOException e) {
            throw new ApiException(e);
        }

        if (respBody == null || "".equals(respBody)) {
            return null;
        }

        String contentType = response.headers().get("Content-Type");
        if (contentType == null) {
            // ensuring a default content type
            contentType = "application/json";
        }
        if (isJsonMime(contentType)) {
            return JSON.deserialize(respBody, returnType);
        } else if (returnType.equals(String.class)) {
            // Expecting string, return the raw response body.
            return (T) respBody;
        } else {
            throw new ApiException(
                    "Content type \"" + contentType + "\" is not supported for type: " + returnType,
                    response.code(),
                    response.headers().toMultimap(),
                    respBody);
        }
    }

    /**
     * Serialize the given Java object into request body according to the object's
     * class and the request Content-Type.
     *
     * @param obj The Java object
     * @param contentType The request Content-Type
     * @return The serialized request body
     * @throws org.openapitools.client.ApiException If fail to serialize the given object
     */
    public RequestBody serialize(Object obj, String contentType) throws ApiException {
        if (obj instanceof byte[]) {
            // Binary (byte array) body parameter support.
            return RequestBody.create((byte[]) obj, MediaType.parse(contentType));
        } else if (obj instanceof File) {
            // File body parameter support.
            return RequestBody.create((File) obj, MediaType.parse(contentType));
        } else if ("text/plain".equals(contentType) && obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else if (isJsonMime(contentType)) {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            return RequestBody.create(content, MediaType.parse(contentType));
        } else if (obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else {
            throw new ApiException("Content type \"" + contentType + "\" is not supported");
        }
    }

    /**
     * Download file from the given response.
     *
     * @param response An instance of the Response object
     * @throws org.openapitools.client.ApiException If fail to read file content from response and write to disk
     * @return Downloaded file
     */
    public File downloadFileFromResponse(Response response) throws ApiException {
        try {
            File file = prepareDownloadFile(response);
            BufferedSink sink = Okio.buffer(Okio.sink(file));
            sink.writeAll(response.body().source());
            sink.close();
            return file;
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * Prepare file for download
     *
     * @param response An instance of the Response object
     * @return Prepared file for the download
     * @throws java.io.IOException If fail to prepare file for download
     */
    public File prepareDownloadFile(Response response) throws IOException {
        String filename = null;
        String contentDisposition = response.header("Content-Disposition");
        if (contentDisposition != null && !"".equals(contentDisposition)) {
            // Get filename from the Content-Disposition header.
            Pattern pattern = Pattern.compile("filename=['\"]?([^'\"\\s]+)['\"]?");
            Matcher matcher = pattern.matcher(contentDisposition);
            if (matcher.find()) {
                filename = sanitizeFilename(matcher.group(1));
            }
        }

        String prefix = null;
        String suffix = null;
        if (filename == null) {
            prefix = "download-";
            suffix = "";
        } else {
            int pos = filename.lastIndexOf(".");
            if (pos == -1) {
                prefix = filename + "-";
            } else {
                prefix = filename.substring(0, pos) + "-";
                suffix = filename.substring(pos);
            }
            // Files.createTempFile requires the prefix to be at least three characters long
            if (prefix.length() < 3)
                prefix = "download-";
        }

        if (tempFolderPath == null)
            return Files.createTempFile(prefix, suffix).toFile();
        else
            return Files.createTempFile(Paths.get(tempFolderPath), prefix, suffix).toFile();
    }

    /**
     * {@link #execute(Call, Type)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @return ApiResponse&lt;T&gt;
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call) throws ApiException {
        return execute(call, null);
    }

    /**
     * Execute HTTP call and deserialize the HTTP response body into the given return type.
     *
     * @param returnType The return type used to deserialize HTTP response body
     * @param <T> The return type corresponding to (same with) returnType
     * @param call Call
     * @return ApiResponse object containing response status, headers and
     *   data, which is a Java object deserialized from response body and would be null
     *   when returnType is null.
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call, Type returnType) throws ApiException {
        try {
            Response response = call.execute();
            T data = handleResponse(response, returnType);
            return new ApiResponse<T>(response.code(), response.headers().toMultimap(), data);
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * {@link #executeAsync(Call, Type, ApiCallback)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @param callback ApiCallback&lt;T&gt;
     */
    public <T> void executeAsync(Call call, ApiCallback<T> callback) {
        executeAsync(call, null, callback);
    }

    /**
     * Execute HTTP call asynchronously.
     *
     * @param <T> Type
     * @param call The callback to be executed when the API call finishes
     * @param returnType Return type
     * @param callback ApiCallback
     * @see #execute(Call, Type)
     */
    @SuppressWarnings("unchecked")
    public <T> void executeAsync(Call call, final Type returnType, final ApiCallback<T> callback) {
        call.enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                callback.onFailure(new ApiException(e), 0, null);
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                T result;
                try {
                    result = (T) handleResponse(response, returnType);
                } catch (ApiException e) {
                    callback.onFailure(e, response.code(), response.headers().toMultimap());
                    return;
                } catch (Exception e) {
                    callback.onFailure(new ApiException(e), response.code(), response.headers().toMultimap());
                    return;
                }
                callback.onSuccess(result, response.code(), response.headers().toMultimap());
            }
        });
    }

    /**
     * Handle the given response, return the deserialized object when the response is successful.
     *
     * @param <T> Type
     * @param response Response
     * @param returnType Return type
     * @return Type
     * @throws org.openapitools.client.ApiException If the response has an unsuccessful status code or
     *                      fail to deserialize the response body
     */
    public <T> T handleResponse(Response response, Type returnType) throws ApiException {
        if (response.isSuccessful()) {
            if (returnType == null || response.code() == 204) {
                // returning null if the returnType is not defined,
                // or the status code is 204 (No Content)
                if (response.body() != null) {
                    try {
                        response.body().close();
                    } catch (Exception e) {
                        throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                    }
                }
                return null;
            } else {
                return deserialize(response, returnType);
            }
        } else {
            String respBody = null;
            if (response.body() != null) {
                try {
                    respBody = response.body().string();
                } catch (IOException e) {
                    throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                }
            }
            throw new ApiException(response.message(), response.code(), response.headers().toMultimap(), respBody);
        }
    }

    /**
     * Build HTTP call with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP call
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Call buildCall(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        Request request = buildRequest(baseUrl, path, method, queryParams, collectionQueryParams, body, headerParams, cookieParams, formParams, authNames, callback);

        return httpClient.newCall(request);
    }

    /**
     * Build an HTTP request with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP request
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Request buildRequest(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        final String url = buildUrl(baseUrl, path, queryParams, collectionQueryParams);

        // prepare HTTP request body
        RequestBody reqBody;
        String contentType = headerParams.get("Content-Type");
        String contentTypePure = contentType;
        if (contentTypePure != null && contentTypePure.contains(";")) {
            contentTypePure = contentType.substring(0, contentType.indexOf(";"));
        }
        if (!HttpMethod.permitsRequestBody(method)) {
            reqBody = null;
        } else if ("application/x-www-form-urlencoded".equals(contentTypePure)) {
            reqBody = buildRequestBodyFormEncoding(formParams);
        } else if ("multipart/form-data".equals(contentTypePure)) {
            reqBody = buildRequestBodyMultipart(formParams);
        } else if (body == null) {
            if ("DELETE".equals(method)) {
                // allow calling DELETE without sending a request body
                reqBody = null;
            } else {
                // use an empty request body (for POST, PUT and PATCH)
                reqBody = RequestBody.create("", contentType == null ? null : MediaType.parse(contentType));
            }
        } else {
            reqBody = serialize(body, contentType);
        }

        List<Pair> updatedQueryParams = new ArrayList<>(queryParams);

        // update parameters with authentication settings
        updateParamsForAuth(authNames, updatedQueryParams, headerParams, cookieParams, requestBodyToString(reqBody), method, URI.create(url));

        final Request.Builder reqBuilder = new Request.Builder().url(buildUrl(baseUrl, path, updatedQueryParams, collectionQueryParams));
        processHeaderParams(headerParams, reqBuilder);
        processCookieParams(cookieParams, reqBuilder);

        // Associate callback with request (if not null) so interceptor can
        // access it when creating ProgressResponseBody
        reqBuilder.tag(callback);

        Request request = null;

        if (callback != null && reqBody != null) {
            ProgressRequestBody progressRequestBody = new ProgressRequestBody(reqBody, callback);
            request = reqBuilder.method(method, progressRequestBody).build();
        } else {
            request = reqBuilder.method(method, reqBody).build();
        }

        return request;
    }

    /**
     * Build full URL by concatenating base path, the given sub path and query parameters.
     *
     * @param baseUrl The base URL
     * @param path The sub path
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @return The full URL
     */
    public String buildUrl(String baseUrl, String path, List<Pair> queryParams, List<Pair> collectionQueryParams) {
        final StringBuilder url = new StringBuilder();
        if (baseUrl != null) {
            url.append(baseUrl).append(path);
        } else {
            String baseURL;
            if (serverIndex != null) {
                if (serverIndex < 0 || serverIndex >= servers.size()) {
                    throw new ArrayIndexOutOfBoundsException(String.format(
                    "Invalid index %d when selecting the host settings. Must be less than %d", serverIndex, servers.size()
                    ));
                }
                baseURL = servers.get(serverIndex).URL(serverVariables);
            } else {
                baseURL = basePath;
            }
            url.append(baseURL).append(path);
        }

        if (queryParams != null && !queryParams.isEmpty()) {
            // support (constant) query string in `path`, e.g. "/posts?draft=1"
            String prefix = path.contains("?") ? "&" : "?";
            for (Pair param : queryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    url.append(escapeString(param.getName())).append("=").append(escapeString(value));
                }
            }
        }

        if (collectionQueryParams != null && !collectionQueryParams.isEmpty()) {
            String prefix = url.toString().contains("?") ? "&" : "?";
            for (Pair param : collectionQueryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    // collection query parameter value already escaped as part of parameterToPairs
                    url.append(escapeString(param.getName())).append("=").append(value);
                }
            }
        }

        return url.toString();
    }

    /**
     * Set header parameters to the request builder, including default headers.
     *
     * @param headerParams Header parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processHeaderParams(Map<String, String> headerParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : headerParams.entrySet()) {
            reqBuilder.header(param.getKey(), parameterToString(param.getValue()));
        }
        for (Entry<String, String> header : defaultHeaderMap.entrySet()) {
            if (!headerParams.containsKey(header.getKey())) {
                reqBuilder.header(header.getKey(), parameterToString(header.getValue()));
            }
        }
    }

    /**
     * Set cookie parameters to the request builder, including default cookies.
     *
     * @param cookieParams Cookie parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processCookieParams(Map<String, String> cookieParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : cookieParams.entrySet()) {
            reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
        }
        for (Entry<String, String> param : defaultCookieMap.entrySet()) {
            if (!cookieParams.containsKey(param.getKey())) {
                reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
            }
        }
    }

    /**
     * Update query and header parameters based on authentication settings.
     *
     * @param authNames The authentications to apply
     * @param queryParams List of query parameters
     * @param headerParams Map of header parameters
     * @param cookieParams Map of cookie parameters
     * @param payload HTTP request body
     * @param method HTTP method
     * @param uri URI
     * @throws org.openapitools.client.ApiException If fails to update the parameters
     */
    public void updateParamsForAuth(String[] authNames, List<Pair> queryParams, Map<String, String> headerParams,
                                    Map<String, String> cookieParams, String payload, String method, URI uri) throws ApiException {
        for (String authName : authNames) {
            Authentication auth = authentications.get(authName);
            if (auth == null) {
                throw new RuntimeException("Authentication undefined: " + authName);
            }
            auth.applyToParams(queryParams, headerParams, cookieParams, payload, method, uri);
        }
    }

    /**
     * Build a form-encoding request body with the given form parameters.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyFormEncoding(Map<String, Object> formParams) {
        okhttp3.FormBody.Builder formBuilder = new okhttp3.FormBody.Builder();
        for (Entry<String, Object> param : formParams.entrySet()) {
            formBuilder.add(param.getKey(), parameterToString(param.getValue()));
        }
        return formBuilder.build();
    }

    /**
     * Build a multipart (file uploading) request body with the given form parameters,
     * which could contain text fields and file fields.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyMultipart(Map<String, Object> formParams) {
        MultipartBody.Builder mpBuilder = new MultipartBody.Builder().setType(MultipartBody.FORM);
        for (Entry<String, Object> param : formParams.entrySet()) {
            if (param.getValue() instanceof File) {
                File file = (File) param.getValue();
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), file);
            } else if (param.getValue() instanceof List) {
                List list = (List) param.getValue();
                for (Object item: list) {
                    if (item instanceof File) {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), (File) item);
                    } else {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
                    }
                }
            } else {
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
            }
        }
        return mpBuilder.build();
    }

    /**
     * Guess Content-Type header from the given file (defaults to "application/octet-stream").
     *
     * @param file The given file
     * @return The guessed Content-Type
     */
    public String guessContentTypeFromFile(File file) {
        String contentType = URLConnection.guessContentTypeFromName(file.getName());
        if (contentType == null) {
            return "application/octet-stream";
        } else {
            return contentType;
        }
    }

    /**
     * Add a Content-Disposition Header for the given key and file to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder 
     * @param key The key of the Header element
     * @param file The file to add to the Header
     */ 
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, File file) {
        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"; filename=\"" + file.getName() + "\"");
        MediaType mediaType = MediaType.parse(guessContentTypeFromFile(file));
        mpBuilder.addPart(partHeaders, RequestBody.create(file, mediaType));
    }

    /**
     * Add a Content-Disposition Header for the given key and complex object to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder
     * @param key The key of the Header element
     * @param obj The complex object to add to the Header
     */
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, Object obj) {
        RequestBody requestBody;
        if (obj instanceof String) {
            requestBody = RequestBody.create((String) obj, MediaType.parse("text/plain"));
        } else {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            requestBody = RequestBody.create(content, MediaType.parse("application/json"));
        }

        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"");
        mpBuilder.addPart(partHeaders, requestBody);
    }

    /**
     * Get network interceptor to add it to the httpClient to track download progress for
     * async requests.
     */
    private Interceptor getProgressInterceptor() {
        return new Interceptor() {
            @Override
            public Response intercept(Interceptor.Chain chain) throws IOException {
                final Request request = chain.request();
                final Response originalResponse = chain.proceed(request);
                if (request.tag() instanceof ApiCallback) {
                    final ApiCallback callback = (ApiCallback) request.tag();
                    return originalResponse.newBuilder()
                        .body(new ProgressResponseBody(originalResponse.body(), callback))
                        .build();
                }
                return originalResponse;
            }
        };
    }

    /**
     * Apply SSL related settings to httpClient according to the current values of
     * verifyingSsl and sslCaCert.
     */
    private void applySslSettings() {
        try {
            TrustManager[] trustManagers;
            HostnameVerifier hostnameVerifier;
            if (!verifyingSsl) {
                trustManagers = new TrustManager[]{
                        new X509TrustManager() {
                            @Override
                            public void checkClientTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public void checkServerTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public java.security.cert.X509Certificate[] getAcceptedIssuers() {
                                return new java.security.cert.X509Certificate[]{};
                            }
                        }
                };
                hostnameVerifier = new HostnameVerifier() {
                    @Override
                    public boolean verify(String hostname, SSLSession session) {
                        return true;
                    }
                };
            } else {
                TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());

                if (sslCaCert == null) {
                    trustManagerFactory.init((KeyStore) null);
                } else {
                    char[] password = null; // Any password will work.
                    CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
                    Collection<? extends Certificate> certificates = certificateFactory.generateCertificates(sslCaCert);
                    if (certificates.isEmpty()) {
                        throw new IllegalArgumentException("expected non-empty set of trusted certificates");
                    }
                    KeyStore caKeyStore = newEmptyKeyStore(password);
                    int index = 0;
                    for (Certificate certificate : certificates) {
                        String certificateAlias = "ca" + (index++);
                        caKeyStore.setCertificateEntry(certificateAlias, certificate);
                    }
                    trustManagerFactory.init(caKeyStore);
                }
                trustManagers = trustManagerFactory.getTrustManagers();
                hostnameVerifier = OkHostnameVerifier.INSTANCE;
            }

            SSLContext sslContext = SSLContext.getInstance("TLS");
            sslContext.init(keyManagers, trustManagers, new SecureRandom());
            httpClient = httpClient.newBuilder()
                            .sslSocketFactory(sslContext.getSocketFactory(), (X509TrustManager) trustManagers[0])
                            .hostnameVerifier(hostnameVerifier)
                            .build();
        } catch (GeneralSecurityException e) {
            throw new RuntimeException(e);
        }
    }

    private KeyStore newEmptyKeyStore(char[] password) throws GeneralSecurityException {
        try {
            KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
            keyStore.load(null, password);
            return keyStore;
        } catch (IOException e) {
            throw new AssertionError(e);
        }
    }

    /**
     * Convert the HTTP request body to a string.
     *
     * @param requestBody The HTTP request object
     * @return The string representation of the HTTP request body
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object into a string
     */
    private String requestBodyToString(RequestBody requestBody) throws ApiException {
        if (requestBody != null) {
            try {
                final Buffer buffer = new Buffer();
                requestBody.writeTo(buffer);
                return buffer.readUtf8();
            } catch (final IOException e) {
                throw new ApiException(e);
            }
        }

        // empty http request body
        return "";
    }
}
