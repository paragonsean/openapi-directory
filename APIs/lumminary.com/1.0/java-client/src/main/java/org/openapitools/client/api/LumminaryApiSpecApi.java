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


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.Authorization;
import org.openapitools.client.model.ClientGene;
import org.openapitools.client.model.ClientSNP;
import java.io.File;
import org.openapitools.client.model.JavascriptWebToken;
import org.openapitools.client.model.Product;
import org.openapitools.client.model.PublicGene;
import org.openapitools.client.model.PublicSNP;
import org.openapitools.client.model.ReferenceChromosomeOverview;
import org.openapitools.client.model.ReferenceGenomeOverview;
import org.openapitools.client.model.ReferenceSequence;
import org.openapitools.client.model.ReportCredentials;
import org.openapitools.client.model.ReportFile;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LumminaryApiSpecApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LumminaryApiSpecApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LumminaryApiSpecApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for getAuthorizationsQueue
     * @param productId The UUID of the product (required)
     * @param seqNumStart The first sequence number from which to fetch (the sequence number of the last processed authorization) (optional)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAuthorizationsQueueCall(String productId, String seqNumStart, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/products/{productId}/authorizations"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (seqNumStart != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("seq_num_start", seqNumStart));
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAuthorizationsQueueValidateBeforeCall(String productId, String seqNumStart, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling getAuthorizationsQueue(Async)");
        }

        return getAuthorizationsQueueCall(productId, seqNumStart, xFields, _callback);

    }

    /**
     * 
     * 
     * @param productId The UUID of the product (required)
     * @param seqNumStart The first sequence number from which to fetch (the sequence number of the last processed authorization) (optional)
     * @param xFields An optional fields mask (optional)
     * @return List&lt;Authorization&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public List<Authorization> getAuthorizationsQueue(String productId, String seqNumStart, String xFields) throws ApiException {
        ApiResponse<List<Authorization>> localVarResp = getAuthorizationsQueueWithHttpInfo(productId, seqNumStart, xFields);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param productId The UUID of the product (required)
     * @param seqNumStart The first sequence number from which to fetch (the sequence number of the last processed authorization) (optional)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;List&lt;Authorization&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Authorization>> getAuthorizationsQueueWithHttpInfo(String productId, String seqNumStart, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getAuthorizationsQueueValidateBeforeCall(productId, seqNumStart, xFields, null);
        Type localVarReturnType = new TypeToken<List<Authorization>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param productId The UUID of the product (required)
     * @param seqNumStart The first sequence number from which to fetch (the sequence number of the last processed authorization) (optional)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAuthorizationsQueueAsync(String productId, String seqNumStart, String xFields, final ApiCallback<List<Authorization>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAuthorizationsQueueValidateBeforeCall(productId, seqNumStart, xFields, _callback);
        Type localVarReturnType = new TypeToken<List<Authorization>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getClientGene
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param geneSymbol The symbol of a gene to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientGeneCall(String clientId, String datasetId, String geneSymbol, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/clients/{clientId}/datasets/{datasetId}/genes/{geneSymbol}"
            .replace("{" + "clientId" + "}", localVarApiClient.escapeString(clientId.toString()))
            .replace("{" + "datasetId" + "}", localVarApiClient.escapeString(datasetId.toString()))
            .replace("{" + "geneSymbol" + "}", localVarApiClient.escapeString(geneSymbol.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getClientGeneValidateBeforeCall(String clientId, String datasetId, String geneSymbol, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clientId' is set
        if (clientId == null) {
            throw new ApiException("Missing the required parameter 'clientId' when calling getClientGene(Async)");
        }

        // verify the required parameter 'datasetId' is set
        if (datasetId == null) {
            throw new ApiException("Missing the required parameter 'datasetId' when calling getClientGene(Async)");
        }

        // verify the required parameter 'geneSymbol' is set
        if (geneSymbol == null) {
            throw new ApiException("Missing the required parameter 'geneSymbol' when calling getClientGene(Async)");
        }

        return getClientGeneCall(clientId, datasetId, geneSymbol, xFields, _callback);

    }

    /**
     * Get gene by symbol
     * Gets A gene by its symbol, which can be found by querying the reference/ resource.  Will return a 404 if a gene exists as a reference, but its genomic coordinates intersect no SNPs in the dataset
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param geneSymbol The symbol of a gene to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @return ClientGene
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ClientGene getClientGene(String clientId, String datasetId, String geneSymbol, String xFields) throws ApiException {
        ApiResponse<ClientGene> localVarResp = getClientGeneWithHttpInfo(clientId, datasetId, geneSymbol, xFields);
        return localVarResp.getData();
    }

    /**
     * Get gene by symbol
     * Gets A gene by its symbol, which can be found by querying the reference/ resource.  Will return a 404 if a gene exists as a reference, but its genomic coordinates intersect no SNPs in the dataset
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param geneSymbol The symbol of a gene to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;ClientGene&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClientGene> getClientGeneWithHttpInfo(String clientId, String datasetId, String geneSymbol, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getClientGeneValidateBeforeCall(clientId, datasetId, geneSymbol, xFields, null);
        Type localVarReturnType = new TypeToken<ClientGene>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get gene by symbol (asynchronously)
     * Gets A gene by its symbol, which can be found by querying the reference/ resource.  Will return a 404 if a gene exists as a reference, but its genomic coordinates intersect no SNPs in the dataset
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param geneSymbol The symbol of a gene to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientGeneAsync(String clientId, String datasetId, String geneSymbol, String xFields, final ApiCallback<ClientGene> _callback) throws ApiException {

        okhttp3.Call localVarCall = getClientGeneValidateBeforeCall(clientId, datasetId, geneSymbol, xFields, _callback);
        Type localVarReturnType = new TypeToken<ClientGene>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getClientSnp
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snpId The rsId of a SNP to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientSnpCall(String clientId, String datasetId, String snpId, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/clients/{clientId}/datasets/{datasetId}/snps/{snpId}"
            .replace("{" + "clientId" + "}", localVarApiClient.escapeString(clientId.toString()))
            .replace("{" + "datasetId" + "}", localVarApiClient.escapeString(datasetId.toString()))
            .replace("{" + "snpId" + "}", localVarApiClient.escapeString(snpId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getClientSnpValidateBeforeCall(String clientId, String datasetId, String snpId, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clientId' is set
        if (clientId == null) {
            throw new ApiException("Missing the required parameter 'clientId' when calling getClientSnp(Async)");
        }

        // verify the required parameter 'datasetId' is set
        if (datasetId == null) {
            throw new ApiException("Missing the required parameter 'datasetId' when calling getClientSnp(Async)");
        }

        // verify the required parameter 'snpId' is set
        if (snpId == null) {
            throw new ApiException("Missing the required parameter 'snpId' when calling getClientSnp(Async)");
        }

        return getClientSnpCall(clientId, datasetId, snpId, xFields, _callback);

    }

    /**
     * Get SNP information
     * Gets SNP information, as provided by the dataset.  If fetching this as an product, the client must have already granted access to the snip (see the &#39;products&#39; group)
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snpId The rsId of a SNP to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @return ClientSNP
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ClientSNP getClientSnp(String clientId, String datasetId, String snpId, String xFields) throws ApiException {
        ApiResponse<ClientSNP> localVarResp = getClientSnpWithHttpInfo(clientId, datasetId, snpId, xFields);
        return localVarResp.getData();
    }

    /**
     * Get SNP information
     * Gets SNP information, as provided by the dataset.  If fetching this as an product, the client must have already granted access to the snip (see the &#39;products&#39; group)
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snpId The rsId of a SNP to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;ClientSNP&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClientSNP> getClientSnpWithHttpInfo(String clientId, String datasetId, String snpId, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getClientSnpValidateBeforeCall(clientId, datasetId, snpId, xFields, null);
        Type localVarReturnType = new TypeToken<ClientSNP>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get SNP information (asynchronously)
     * Gets SNP information, as provided by the dataset.  If fetching this as an product, the client must have already granted access to the snip (see the &#39;products&#39; group)
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snpId The rsId of a SNP to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientSnpAsync(String clientId, String datasetId, String snpId, String xFields, final ApiCallback<ClientSNP> _callback) throws ApiException {

        okhttp3.Call localVarCall = getClientSnpValidateBeforeCall(clientId, datasetId, snpId, xFields, _callback);
        Type localVarReturnType = new TypeToken<ClientSNP>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getClientSnpGroup
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientSnpGroupCall(String clientId, String datasetId, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/clients/{clientId}/datasets/{datasetId}/snps/"
            .replace("{" + "clientId" + "}", localVarApiClient.escapeString(clientId.toString()))
            .replace("{" + "datasetId" + "}", localVarApiClient.escapeString(datasetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getClientSnpGroupValidateBeforeCall(String clientId, String datasetId, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clientId' is set
        if (clientId == null) {
            throw new ApiException("Missing the required parameter 'clientId' when calling getClientSnpGroup(Async)");
        }

        // verify the required parameter 'datasetId' is set
        if (datasetId == null) {
            throw new ApiException("Missing the required parameter 'datasetId' when calling getClientSnpGroup(Async)");
        }

        return getClientSnpGroupCall(clientId, datasetId, xFields, _callback);

    }

    /**
     * 
     * 
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param xFields An optional fields mask (optional)
     * @return List&lt;ClientSNP&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public List<ClientSNP> getClientSnpGroup(String clientId, String datasetId, String xFields) throws ApiException {
        ApiResponse<List<ClientSNP>> localVarResp = getClientSnpGroupWithHttpInfo(clientId, datasetId, xFields);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;List&lt;ClientSNP&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ClientSNP>> getClientSnpGroupWithHttpInfo(String clientId, String datasetId, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getClientSnpGroupValidateBeforeCall(clientId, datasetId, xFields, null);
        Type localVarReturnType = new TypeToken<List<ClientSNP>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClientSnpGroupAsync(String clientId, String datasetId, String xFields, final ApiCallback<List<ClientSNP>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getClientSnpGroupValidateBeforeCall(clientId, datasetId, xFields, _callback);
        Type localVarReturnType = new TypeToken<List<ClientSNP>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getGene
     * @param databaseName The name of the database to search. E.g: Genbank (required)
     * @param accession The accession within the selected database (required)
     * @param dbsnpBuild The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 (optional, default to 149)
     * @param referenceGenome The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getGeneCall(String databaseName, String accession, Integer dbsnpBuild, String referenceGenome, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/reference/genes/databases/{databaseName}/accessions/{accession}"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName.toString()))
            .replace("{" + "accession" + "}", localVarApiClient.escapeString(accession.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dbsnpBuild != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("dbsnp_build", dbsnpBuild));
        }

        if (referenceGenome != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("reference_genome", referenceGenome));
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getGeneValidateBeforeCall(String databaseName, String accession, Integer dbsnpBuild, String referenceGenome, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling getGene(Async)");
        }

        // verify the required parameter 'accession' is set
        if (accession == null) {
            throw new ApiException("Missing the required parameter 'accession' when calling getGene(Async)");
        }

        return getGeneCall(databaseName, accession, dbsnpBuild, referenceGenome, xFields, _callback);

    }

    /**
     * Generic gene information
     * 
     * @param databaseName The name of the database to search. E.g: Genbank (required)
     * @param accession The accession within the selected database (required)
     * @param dbsnpBuild The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 (optional, default to 149)
     * @param referenceGenome The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @return PublicGene
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public PublicGene getGene(String databaseName, String accession, Integer dbsnpBuild, String referenceGenome, String xFields) throws ApiException {
        ApiResponse<PublicGene> localVarResp = getGeneWithHttpInfo(databaseName, accession, dbsnpBuild, referenceGenome, xFields);
        return localVarResp.getData();
    }

    /**
     * Generic gene information
     * 
     * @param databaseName The name of the database to search. E.g: Genbank (required)
     * @param accession The accession within the selected database (required)
     * @param dbsnpBuild The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 (optional, default to 149)
     * @param referenceGenome The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;PublicGene&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PublicGene> getGeneWithHttpInfo(String databaseName, String accession, Integer dbsnpBuild, String referenceGenome, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getGeneValidateBeforeCall(databaseName, accession, dbsnpBuild, referenceGenome, xFields, null);
        Type localVarReturnType = new TypeToken<PublicGene>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Generic gene information (asynchronously)
     * 
     * @param databaseName The name of the database to search. E.g: Genbank (required)
     * @param accession The accession within the selected database (required)
     * @param dbsnpBuild The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 (optional, default to 149)
     * @param referenceGenome The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getGeneAsync(String databaseName, String accession, Integer dbsnpBuild, String referenceGenome, String xFields, final ApiCallback<PublicGene> _callback) throws ApiException {

        okhttp3.Call localVarCall = getGeneValidateBeforeCall(databaseName, accession, dbsnpBuild, referenceGenome, xFields, _callback);
        Type localVarReturnType = new TypeToken<PublicGene>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProduct
     * @param productId The UUID of the product (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProductCall(String productId, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/products/{productId}"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getProductValidateBeforeCall(String productId, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling getProduct(Async)");
        }

        return getProductCall(productId, xFields, _callback);

    }

    /**
     * Get product details
     * 
     * @param productId The UUID of the product (required)
     * @param xFields An optional fields mask (optional)
     * @return Product
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public Product getProduct(String productId, String xFields) throws ApiException {
        ApiResponse<Product> localVarResp = getProductWithHttpInfo(productId, xFields);
        return localVarResp.getData();
    }

    /**
     * Get product details
     * 
     * @param productId The UUID of the product (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;Product&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Product> getProductWithHttpInfo(String productId, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getProductValidateBeforeCall(productId, xFields, null);
        Type localVarReturnType = new TypeToken<Product>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get product details (asynchronously)
     * 
     * @param productId The UUID of the product (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProductAsync(String productId, String xFields, final ApiCallback<Product> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProductValidateBeforeCall(productId, xFields, _callback);
        Type localVarReturnType = new TypeToken<Product>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProductAuthorization
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProductAuthorizationCall(String productId, String authorizationId, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/products/{productId}/authorizations/{authorizationId}"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "authorizationId" + "}", localVarApiClient.escapeString(authorizationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getProductAuthorizationValidateBeforeCall(String productId, String authorizationId, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling getProductAuthorization(Async)");
        }

        // verify the required parameter 'authorizationId' is set
        if (authorizationId == null) {
            throw new ApiException("Missing the required parameter 'authorizationId' when calling getProductAuthorization(Async)");
        }

        return getProductAuthorizationCall(productId, authorizationId, xFields, _callback);

    }

    /**
     * 
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @return Authorization
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public Authorization getProductAuthorization(String productId, String authorizationId, String xFields) throws ApiException {
        ApiResponse<Authorization> localVarResp = getProductAuthorizationWithHttpInfo(productId, authorizationId, xFields);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;Authorization&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Authorization> getProductAuthorizationWithHttpInfo(String productId, String authorizationId, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getProductAuthorizationValidateBeforeCall(productId, authorizationId, xFields, null);
        Type localVarReturnType = new TypeToken<Authorization>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProductAuthorizationAsync(String productId, String authorizationId, String xFields, final ApiCallback<Authorization> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProductAuthorizationValidateBeforeCall(productId, authorizationId, xFields, _callback);
        Type localVarReturnType = new TypeToken<Authorization>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getReferenceChromosome
     * @param genomeBuildAccession The accession of the reference genome (required)
     * @param chromosomeAccession The accession to the chromosome (required)
     * @param rangeStart Location on the chromosome (required)
     * @param rangeStop Location on the chromosome (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceChromosomeCall(String genomeBuildAccession, String chromosomeAccession, Integer rangeStart, Integer rangeStop, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/reference/genomes/{genomeBuildAccession}/chromosomes/{chromosomeAccession}"
            .replace("{" + "genomeBuildAccession" + "}", localVarApiClient.escapeString(genomeBuildAccession.toString()))
            .replace("{" + "chromosomeAccession" + "}", localVarApiClient.escapeString(chromosomeAccession.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (rangeStart != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("range_start", rangeStart));
        }

        if (rangeStop != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("range_stop", rangeStop));
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getReferenceChromosomeValidateBeforeCall(String genomeBuildAccession, String chromosomeAccession, Integer rangeStart, Integer rangeStop, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'genomeBuildAccession' is set
        if (genomeBuildAccession == null) {
            throw new ApiException("Missing the required parameter 'genomeBuildAccession' when calling getReferenceChromosome(Async)");
        }

        // verify the required parameter 'chromosomeAccession' is set
        if (chromosomeAccession == null) {
            throw new ApiException("Missing the required parameter 'chromosomeAccession' when calling getReferenceChromosome(Async)");
        }

        // verify the required parameter 'rangeStart' is set
        if (rangeStart == null) {
            throw new ApiException("Missing the required parameter 'rangeStart' when calling getReferenceChromosome(Async)");
        }

        // verify the required parameter 'rangeStop' is set
        if (rangeStop == null) {
            throw new ApiException("Missing the required parameter 'rangeStop' when calling getReferenceChromosome(Async)");
        }

        return getReferenceChromosomeCall(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, xFields, _callback);

    }

    /**
     * Sequence for a region of the reference genome
     * Fetch a closed interval of nucleotides on a given chromosome. Includes start and stop positions
     * @param genomeBuildAccession The accession of the reference genome (required)
     * @param chromosomeAccession The accession to the chromosome (required)
     * @param rangeStart Location on the chromosome (required)
     * @param rangeStop Location on the chromosome (required)
     * @param xFields An optional fields mask (optional)
     * @return ReferenceSequence
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ReferenceSequence getReferenceChromosome(String genomeBuildAccession, String chromosomeAccession, Integer rangeStart, Integer rangeStop, String xFields) throws ApiException {
        ApiResponse<ReferenceSequence> localVarResp = getReferenceChromosomeWithHttpInfo(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, xFields);
        return localVarResp.getData();
    }

    /**
     * Sequence for a region of the reference genome
     * Fetch a closed interval of nucleotides on a given chromosome. Includes start and stop positions
     * @param genomeBuildAccession The accession of the reference genome (required)
     * @param chromosomeAccession The accession to the chromosome (required)
     * @param rangeStart Location on the chromosome (required)
     * @param rangeStop Location on the chromosome (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;ReferenceSequence&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReferenceSequence> getReferenceChromosomeWithHttpInfo(String genomeBuildAccession, String chromosomeAccession, Integer rangeStart, Integer rangeStop, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getReferenceChromosomeValidateBeforeCall(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, xFields, null);
        Type localVarReturnType = new TypeToken<ReferenceSequence>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Sequence for a region of the reference genome (asynchronously)
     * Fetch a closed interval of nucleotides on a given chromosome. Includes start and stop positions
     * @param genomeBuildAccession The accession of the reference genome (required)
     * @param chromosomeAccession The accession to the chromosome (required)
     * @param rangeStart Location on the chromosome (required)
     * @param rangeStop Location on the chromosome (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceChromosomeAsync(String genomeBuildAccession, String chromosomeAccession, Integer rangeStart, Integer rangeStop, String xFields, final ApiCallback<ReferenceSequence> _callback) throws ApiException {

        okhttp3.Call localVarCall = getReferenceChromosomeValidateBeforeCall(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, xFields, _callback);
        Type localVarReturnType = new TypeToken<ReferenceSequence>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getReferenceGenome
     * @param genomeBuildAccession  (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceGenomeCall(String genomeBuildAccession, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/reference/genomes/{genomeBuildAccession}/chromosomes"
            .replace("{" + "genomeBuildAccession" + "}", localVarApiClient.escapeString(genomeBuildAccession.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getReferenceGenomeValidateBeforeCall(String genomeBuildAccession, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'genomeBuildAccession' is set
        if (genomeBuildAccession == null) {
            throw new ApiException("Missing the required parameter 'genomeBuildAccession' when calling getReferenceGenome(Async)");
        }

        return getReferenceGenomeCall(genomeBuildAccession, xFields, _callback);

    }

    /**
     * Reference genome metadata
     * 
     * @param genomeBuildAccession  (required)
     * @param xFields An optional fields mask (optional)
     * @return List&lt;ReferenceChromosomeOverview&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public List<ReferenceChromosomeOverview> getReferenceGenome(String genomeBuildAccession, String xFields) throws ApiException {
        ApiResponse<List<ReferenceChromosomeOverview>> localVarResp = getReferenceGenomeWithHttpInfo(genomeBuildAccession, xFields);
        return localVarResp.getData();
    }

    /**
     * Reference genome metadata
     * 
     * @param genomeBuildAccession  (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;List&lt;ReferenceChromosomeOverview&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ReferenceChromosomeOverview>> getReferenceGenomeWithHttpInfo(String genomeBuildAccession, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getReferenceGenomeValidateBeforeCall(genomeBuildAccession, xFields, null);
        Type localVarReturnType = new TypeToken<List<ReferenceChromosomeOverview>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reference genome metadata (asynchronously)
     * 
     * @param genomeBuildAccession  (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceGenomeAsync(String genomeBuildAccession, String xFields, final ApiCallback<List<ReferenceChromosomeOverview>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getReferenceGenomeValidateBeforeCall(genomeBuildAccession, xFields, _callback);
        Type localVarReturnType = new TypeToken<List<ReferenceChromosomeOverview>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getReferenceGenomesGroup
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceGenomesGroupCall(String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/reference/genomes/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getReferenceGenomesGroupValidateBeforeCall(String xFields, final ApiCallback _callback) throws ApiException {
        return getReferenceGenomesGroupCall(xFields, _callback);

    }

    /**
     * Reference genome builds
     * Lists reference genome builds that are available
     * @param xFields An optional fields mask (optional)
     * @return List&lt;ReferenceGenomeOverview&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public List<ReferenceGenomeOverview> getReferenceGenomesGroup(String xFields) throws ApiException {
        ApiResponse<List<ReferenceGenomeOverview>> localVarResp = getReferenceGenomesGroupWithHttpInfo(xFields);
        return localVarResp.getData();
    }

    /**
     * Reference genome builds
     * Lists reference genome builds that are available
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;List&lt;ReferenceGenomeOverview&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ReferenceGenomeOverview>> getReferenceGenomesGroupWithHttpInfo(String xFields) throws ApiException {
        okhttp3.Call localVarCall = getReferenceGenomesGroupValidateBeforeCall(xFields, null);
        Type localVarReturnType = new TypeToken<List<ReferenceGenomeOverview>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reference genome builds (asynchronously)
     * Lists reference genome builds that are available
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceGenomesGroupAsync(String xFields, final ApiCallback<List<ReferenceGenomeOverview>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getReferenceGenomesGroupValidateBeforeCall(xFields, _callback);
        Type localVarReturnType = new TypeToken<List<ReferenceGenomeOverview>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getReferenceSnp
     * @param snpAccession The rsId of the SNP (required)
     * @param dbsnpVersion The dbSNP build. Defaults to 149 (optional, default to 149)
     * @param grchVersion The GRCh build on which to place snips. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceSnpCall(String snpAccession, Integer dbsnpVersion, String grchVersion, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/reference/snps/{snpAccession}"
            .replace("{" + "snpAccession" + "}", localVarApiClient.escapeString(snpAccession.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dbsnpVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("dbsnp_version", dbsnpVersion));
        }

        if (grchVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("grch_version", grchVersion));
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getReferenceSnpValidateBeforeCall(String snpAccession, Integer dbsnpVersion, String grchVersion, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'snpAccession' is set
        if (snpAccession == null) {
            throw new ApiException("Missing the required parameter 'snpAccession' when calling getReferenceSnp(Async)");
        }

        return getReferenceSnpCall(snpAccession, dbsnpVersion, grchVersion, xFields, _callback);

    }

    /**
     * Reference SNP data
     * Get reference SNP information, from dbSNP
     * @param snpAccession The rsId of the SNP (required)
     * @param dbsnpVersion The dbSNP build. Defaults to 149 (optional, default to 149)
     * @param grchVersion The GRCh build on which to place snips. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @return PublicSNP
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public PublicSNP getReferenceSnp(String snpAccession, Integer dbsnpVersion, String grchVersion, String xFields) throws ApiException {
        ApiResponse<PublicSNP> localVarResp = getReferenceSnpWithHttpInfo(snpAccession, dbsnpVersion, grchVersion, xFields);
        return localVarResp.getData();
    }

    /**
     * Reference SNP data
     * Get reference SNP information, from dbSNP
     * @param snpAccession The rsId of the SNP (required)
     * @param dbsnpVersion The dbSNP build. Defaults to 149 (optional, default to 149)
     * @param grchVersion The GRCh build on which to place snips. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;PublicSNP&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PublicSNP> getReferenceSnpWithHttpInfo(String snpAccession, Integer dbsnpVersion, String grchVersion, String xFields) throws ApiException {
        okhttp3.Call localVarCall = getReferenceSnpValidateBeforeCall(snpAccession, dbsnpVersion, grchVersion, xFields, null);
        Type localVarReturnType = new TypeToken<PublicSNP>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reference SNP data (asynchronously)
     * Get reference SNP information, from dbSNP
     * @param snpAccession The rsId of the SNP (required)
     * @param dbsnpVersion The dbSNP build. Defaults to 149 (optional, default to 149)
     * @param grchVersion The GRCh build on which to place snips. Defaults to GRCh37p13 (optional, default to GRCH37P13)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getReferenceSnpAsync(String snpAccession, Integer dbsnpVersion, String grchVersion, String xFields, final ApiCallback<PublicSNP> _callback) throws ApiException {

        okhttp3.Call localVarCall = getReferenceSnpValidateBeforeCall(snpAccession, dbsnpVersion, grchVersion, xFields, _callback);
        Type localVarReturnType = new TypeToken<PublicSNP>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postAuthorizationResultCredentials
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @param credentialsUsername Credentials for accessing the result. Includes password, username and url (optional)
     * @param credentialsPassword Credentials for accessing the result. Includes password, username and url (optional)
     * @param reportUrl Credentials for accessing the result. Includes password, username and url (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAuthorizationResultCredentialsCall(String productId, String authorizationId, String xFields, String credentialsUsername, String credentialsPassword, String reportUrl, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/products/{productId}/authorizations/{authorizationId}/credentials"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "authorizationId" + "}", localVarApiClient.escapeString(authorizationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (credentialsUsername != null) {
            localVarFormParams.put("credentials_username", credentialsUsername);
        }

        if (credentialsPassword != null) {
            localVarFormParams.put("credentials_password", credentialsPassword);
        }

        if (reportUrl != null) {
            localVarFormParams.put("report_url", reportUrl);
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/x-www-form-urlencoded",
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postAuthorizationResultCredentialsValidateBeforeCall(String productId, String authorizationId, String xFields, String credentialsUsername, String credentialsPassword, String reportUrl, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling postAuthorizationResultCredentials(Async)");
        }

        // verify the required parameter 'authorizationId' is set
        if (authorizationId == null) {
            throw new ApiException("Missing the required parameter 'authorizationId' when calling postAuthorizationResultCredentials(Async)");
        }

        return postAuthorizationResultCredentialsCall(productId, authorizationId, xFields, credentialsUsername, credentialsPassword, reportUrl, _callback);

    }

    /**
     * Provide a result for the authorization
     * These can be log-in credentials for a website where the result is available
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @param credentialsUsername Credentials for accessing the result. Includes password, username and url (optional)
     * @param credentialsPassword Credentials for accessing the result. Includes password, username and url (optional)
     * @param reportUrl Credentials for accessing the result. Includes password, username and url (optional)
     * @return ReportCredentials
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ReportCredentials postAuthorizationResultCredentials(String productId, String authorizationId, String xFields, String credentialsUsername, String credentialsPassword, String reportUrl) throws ApiException {
        ApiResponse<ReportCredentials> localVarResp = postAuthorizationResultCredentialsWithHttpInfo(productId, authorizationId, xFields, credentialsUsername, credentialsPassword, reportUrl);
        return localVarResp.getData();
    }

    /**
     * Provide a result for the authorization
     * These can be log-in credentials for a website where the result is available
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @param credentialsUsername Credentials for accessing the result. Includes password, username and url (optional)
     * @param credentialsPassword Credentials for accessing the result. Includes password, username and url (optional)
     * @param reportUrl Credentials for accessing the result. Includes password, username and url (optional)
     * @return ApiResponse&lt;ReportCredentials&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReportCredentials> postAuthorizationResultCredentialsWithHttpInfo(String productId, String authorizationId, String xFields, String credentialsUsername, String credentialsPassword, String reportUrl) throws ApiException {
        okhttp3.Call localVarCall = postAuthorizationResultCredentialsValidateBeforeCall(productId, authorizationId, xFields, credentialsUsername, credentialsPassword, reportUrl, null);
        Type localVarReturnType = new TypeToken<ReportCredentials>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Provide a result for the authorization (asynchronously)
     * These can be log-in credentials for a website where the result is available
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param xFields An optional fields mask (optional)
     * @param credentialsUsername Credentials for accessing the result. Includes password, username and url (optional)
     * @param credentialsPassword Credentials for accessing the result. Includes password, username and url (optional)
     * @param reportUrl Credentials for accessing the result. Includes password, username and url (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAuthorizationResultCredentialsAsync(String productId, String authorizationId, String xFields, String credentialsUsername, String credentialsPassword, String reportUrl, final ApiCallback<ReportCredentials> _callback) throws ApiException {

        okhttp3.Call localVarCall = postAuthorizationResultCredentialsValidateBeforeCall(productId, authorizationId, xFields, credentialsUsername, credentialsPassword, reportUrl, _callback);
        Type localVarReturnType = new TypeToken<ReportCredentials>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postAuthorizationResultFile
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param originalFilename Optional original filename for the report. If not provided, the filename of uploaded file will be used (optional)
     * @param xFields An optional fields mask (optional)
     * @param fileReport A binary file (e.g. pdf) that contains the result of the authorization (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAuthorizationResultFileCall(String productId, String authorizationId, String originalFilename, String xFields, File fileReport, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/products/{productId}/authorizations/{authorizationId}/file"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "authorizationId" + "}", localVarApiClient.escapeString(authorizationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (fileReport != null) {
            localVarFormParams.put("file_report", fileReport);
        }

        if (originalFilename != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("original_filename", originalFilename));
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postAuthorizationResultFileValidateBeforeCall(String productId, String authorizationId, String originalFilename, String xFields, File fileReport, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling postAuthorizationResultFile(Async)");
        }

        // verify the required parameter 'authorizationId' is set
        if (authorizationId == null) {
            throw new ApiException("Missing the required parameter 'authorizationId' when calling postAuthorizationResultFile(Async)");
        }

        return postAuthorizationResultFileCall(productId, authorizationId, originalFilename, xFields, fileReport, _callback);

    }

    /**
     * Provide a file result to the authorization, e
     * g. a pdf report
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param originalFilename Optional original filename for the report. If not provided, the filename of uploaded file will be used (optional)
     * @param xFields An optional fields mask (optional)
     * @param fileReport A binary file (e.g. pdf) that contains the result of the authorization (optional)
     * @return ReportFile
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ReportFile postAuthorizationResultFile(String productId, String authorizationId, String originalFilename, String xFields, File fileReport) throws ApiException {
        ApiResponse<ReportFile> localVarResp = postAuthorizationResultFileWithHttpInfo(productId, authorizationId, originalFilename, xFields, fileReport);
        return localVarResp.getData();
    }

    /**
     * Provide a file result to the authorization, e
     * g. a pdf report
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param originalFilename Optional original filename for the report. If not provided, the filename of uploaded file will be used (optional)
     * @param xFields An optional fields mask (optional)
     * @param fileReport A binary file (e.g. pdf) that contains the result of the authorization (optional)
     * @return ApiResponse&lt;ReportFile&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReportFile> postAuthorizationResultFileWithHttpInfo(String productId, String authorizationId, String originalFilename, String xFields, File fileReport) throws ApiException {
        okhttp3.Call localVarCall = postAuthorizationResultFileValidateBeforeCall(productId, authorizationId, originalFilename, xFields, fileReport, null);
        Type localVarReturnType = new TypeToken<ReportFile>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Provide a file result to the authorization, e (asynchronously)
     * g. a pdf report
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param originalFilename Optional original filename for the report. If not provided, the filename of uploaded file will be used (optional)
     * @param xFields An optional fields mask (optional)
     * @param fileReport A binary file (e.g. pdf) that contains the result of the authorization (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postAuthorizationResultFileAsync(String productId, String authorizationId, String originalFilename, String xFields, File fileReport, final ApiCallback<ReportFile> _callback) throws ApiException {

        okhttp3.Call localVarCall = postAuthorizationResultFileValidateBeforeCall(productId, authorizationId, originalFilename, xFields, fileReport, _callback);
        Type localVarReturnType = new TypeToken<ReportFile>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postClientSnpGroup
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snps JSON-encoded list of snps to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postClientSnpGroupCall(String clientId, String datasetId, String snps, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/clients/{clientId}/datasets/{datasetId}/snps/"
            .replace("{" + "clientId" + "}", localVarApiClient.escapeString(clientId.toString()))
            .replace("{" + "datasetId" + "}", localVarApiClient.escapeString(datasetId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (snps != null) {
            localVarFormParams.put("snps", snps);
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/x-www-form-urlencoded",
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postClientSnpGroupValidateBeforeCall(String clientId, String datasetId, String snps, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clientId' is set
        if (clientId == null) {
            throw new ApiException("Missing the required parameter 'clientId' when calling postClientSnpGroup(Async)");
        }

        // verify the required parameter 'datasetId' is set
        if (datasetId == null) {
            throw new ApiException("Missing the required parameter 'datasetId' when calling postClientSnpGroup(Async)");
        }

        // verify the required parameter 'snps' is set
        if (snps == null) {
            throw new ApiException("Missing the required parameter 'snps' when calling postClientSnpGroup(Async)");
        }

        return postClientSnpGroupCall(clientId, datasetId, snps, xFields, _callback);

    }

    /**
     * Get a large group of SNPs
     * SNPs that are not present in the dataset are ignored, 404 is returned only if the dataset/client does not exist
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snps JSON-encoded list of snps to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @return List&lt;ClientSNP&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public List<ClientSNP> postClientSnpGroup(String clientId, String datasetId, String snps, String xFields) throws ApiException {
        ApiResponse<List<ClientSNP>> localVarResp = postClientSnpGroupWithHttpInfo(clientId, datasetId, snps, xFields);
        return localVarResp.getData();
    }

    /**
     * Get a large group of SNPs
     * SNPs that are not present in the dataset are ignored, 404 is returned only if the dataset/client does not exist
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snps JSON-encoded list of snps to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;List&lt;ClientSNP&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ClientSNP>> postClientSnpGroupWithHttpInfo(String clientId, String datasetId, String snps, String xFields) throws ApiException {
        okhttp3.Call localVarCall = postClientSnpGroupValidateBeforeCall(clientId, datasetId, snps, xFields, null);
        Type localVarReturnType = new TypeToken<List<ClientSNP>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a large group of SNPs (asynchronously)
     * SNPs that are not present in the dataset are ignored, 404 is returned only if the dataset/client does not exist
     * @param clientId The UUID of the client (required)
     * @param datasetId The UUID of one of the client&#39;s dataset (required)
     * @param snps JSON-encoded list of snps to be fetched (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postClientSnpGroupAsync(String clientId, String datasetId, String snps, String xFields, final ApiCallback<List<ClientSNP>> _callback) throws ApiException {

        okhttp3.Call localVarCall = postClientSnpGroupValidateBeforeCall(clientId, datasetId, snps, xFields, _callback);
        Type localVarReturnType = new TypeToken<List<ClientSNP>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postJwtAuth
     * @param username The email for a Client, or the API for a partner product (required)
     * @param password The passowrd for a Client, or the API key for a service (required)
     * @param role The role for which authentication will be made. Value : role_product (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postJwtAuthCall(String username, String password, String role, String xFields, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/auth/jwt";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (username != null) {
            localVarFormParams.put("username", username);
        }

        if (password != null) {
            localVarFormParams.put("password", password);
        }

        if (role != null) {
            localVarFormParams.put("role", role);
        }

        if (xFields != null) {
            localVarHeaderParams.put("X-Fields", localVarApiClient.parameterToString(xFields));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/x-www-form-urlencoded",
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postJwtAuthValidateBeforeCall(String username, String password, String role, String xFields, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'username' is set
        if (username == null) {
            throw new ApiException("Missing the required parameter 'username' when calling postJwtAuth(Async)");
        }

        // verify the required parameter 'password' is set
        if (password == null) {
            throw new ApiException("Missing the required parameter 'password' when calling postJwtAuth(Async)");
        }

        // verify the required parameter 'role' is set
        if (role == null) {
            throw new ApiException("Missing the required parameter 'role' when calling postJwtAuth(Async)");
        }

        return postJwtAuthCall(username, password, role, xFields, _callback);

    }

    /**
     * General-purpose authentication
     * ## Note: * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format &#x60;Bearer: your-token-here&#x60; * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued
     * @param username The email for a Client, or the API for a partner product (required)
     * @param password The passowrd for a Client, or the API key for a service (required)
     * @param role The role for which authentication will be made. Value : role_product (required)
     * @param xFields An optional fields mask (optional)
     * @return JavascriptWebToken
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public JavascriptWebToken postJwtAuth(String username, String password, String role, String xFields) throws ApiException {
        ApiResponse<JavascriptWebToken> localVarResp = postJwtAuthWithHttpInfo(username, password, role, xFields);
        return localVarResp.getData();
    }

    /**
     * General-purpose authentication
     * ## Note: * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format &#x60;Bearer: your-token-here&#x60; * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued
     * @param username The email for a Client, or the API for a partner product (required)
     * @param password The passowrd for a Client, or the API key for a service (required)
     * @param role The role for which authentication will be made. Value : role_product (required)
     * @param xFields An optional fields mask (optional)
     * @return ApiResponse&lt;JavascriptWebToken&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<JavascriptWebToken> postJwtAuthWithHttpInfo(String username, String password, String role, String xFields) throws ApiException {
        okhttp3.Call localVarCall = postJwtAuthValidateBeforeCall(username, password, role, xFields, null);
        Type localVarReturnType = new TypeToken<JavascriptWebToken>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * General-purpose authentication (asynchronously)
     * ## Note: * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format &#x60;Bearer: your-token-here&#x60; * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued
     * @param username The email for a Client, or the API for a partner product (required)
     * @param password The passowrd for a Client, or the API key for a service (required)
     * @param role The role for which authentication will be made. Value : role_product (required)
     * @param xFields An optional fields mask (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postJwtAuthAsync(String username, String password, String role, String xFields, final ApiCallback<JavascriptWebToken> _callback) throws ApiException {

        okhttp3.Call localVarCall = postJwtAuthValidateBeforeCall(username, password, role, xFields, _callback);
        Type localVarReturnType = new TypeToken<JavascriptWebToken>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postProductAuthorization
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postProductAuthorizationCall(String productId, String authorizationId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/products/{productId}/authorizations/{authorizationId}"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "authorizationId" + "}", localVarApiClient.escapeString(authorizationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postProductAuthorizationValidateBeforeCall(String productId, String authorizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling postProductAuthorization(Async)");
        }

        // verify the required parameter 'authorizationId' is set
        if (authorizationId == null) {
            throw new ApiException("Missing the required parameter 'authorizationId' when calling postProductAuthorization(Async)");
        }

        return postProductAuthorizationCall(productId, authorizationId, _callback);

    }

    /**
     * Signal that processing is complete, without uploading any result
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public void postProductAuthorization(String productId, String authorizationId) throws ApiException {
        postProductAuthorizationWithHttpInfo(productId, authorizationId);
    }

    /**
     * Signal that processing is complete, without uploading any result
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> postProductAuthorizationWithHttpInfo(String productId, String authorizationId) throws ApiException {
        okhttp3.Call localVarCall = postProductAuthorizationValidateBeforeCall(productId, authorizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Signal that processing is complete, without uploading any result (asynchronously)
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Result saved </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postProductAuthorizationAsync(String productId, String authorizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = postProductAuthorizationValidateBeforeCall(productId, authorizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for postProductAuthorizationUnfulfillable
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postProductAuthorizationUnfulfillableCall(String productId, String authorizationId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/products/{productId}/authorizations/{authorizationId}/unfulfillable"
            .replace("{" + "productId" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "authorizationId" + "}", localVarApiClient.escapeString(authorizationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "Bearer" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postProductAuthorizationUnfulfillableValidateBeforeCall(String productId, String authorizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling postProductAuthorizationUnfulfillable(Async)");
        }

        // verify the required parameter 'authorizationId' is set
        if (authorizationId == null) {
            throw new ApiException("Missing the required parameter 'authorizationId' when calling postProductAuthorizationUnfulfillable(Async)");
        }

        return postProductAuthorizationUnfulfillableCall(productId, authorizationId, _callback);

    }

    /**
     * Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public void postProductAuthorizationUnfulfillable(String productId, String authorizationId) throws ApiException {
        postProductAuthorizationUnfulfillableWithHttpInfo(productId, authorizationId);
    }

    /**
     * Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> postProductAuthorizationUnfulfillableWithHttpInfo(String productId, String authorizationId) throws ApiException {
        okhttp3.Call localVarCall = postProductAuthorizationUnfulfillableValidateBeforeCall(productId, authorizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons (asynchronously)
     * 
     * @param productId The UUID of the product (required)
     * @param authorizationId The UUID of the authorization (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 404 </td><td> Object not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postProductAuthorizationUnfulfillableAsync(String productId, String authorizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = postProductAuthorizationUnfulfillableValidateBeforeCall(productId, authorizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
