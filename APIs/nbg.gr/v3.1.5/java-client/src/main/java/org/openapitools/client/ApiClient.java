/*
 * Account and Transaction API Specification - UK
 * ## Functionality at a glance    The NBG \"UK OPB - Account and Transaction v3.1.5\" API follows the [UK Open Banking Specification      v3.1.5](https://openbankinguk.github.io/read-write-api-site3/v3.1.5/profiles/account-and-transaction-api-profile.html)    This Account and Transaction API Specification describes the flows and payloads for retrieving a list of accounts and their transactions.    The API endpoints described here allow a AISP to:      * Create the Consent with the appropriate permissions in order to be able to access the API Endpoints    * Retrieve the list of accounts    * Retrieve an account's details    * Retrieve an account's balances    * Retrieve an account's transactions    * Retrieve an account's beneficiaries    * Retrieve an account's standing orders    * Retrieve an account's party    * Retrieve an account's scheduled payments    * Retrieve an account's statements        ## Quick Getting Started      1. **Login/Register** to the NBG Technology HUB    2. Go to **\"APPS\"**    3. Select your Organization and go to step 4. If you want to create a new Organization click **\\\"CREATE AN ORGANIZATION\\\"** and follow the steps below:   1. Enter the title of your Organization   2. Enter a short description of your Organization (optional)   3. Click **\"SUBMIT\"**    4. Select the Organization of choice and click **\"ADD AN APPLICATION\"**      1. Fill in the forms (title and short description)     2. Check **\\\"Authorization Code\\\" and \\\"Client Credentials\\\"**      3. Enter the **OAuth Redirect and Post Logout URIs** (these are the URIs that we will redirect the user upon logging in and logging out respectively)            You can use the following redirect URL to easily test the API through the portal: *https://developer.nbg.gr/oauth2/redoc-callback*     4. Click **\"SUBMIT\"**     5. Store the APPs **\"Client ID\"** and **\"Client Secret\"**  5. Go to **\"API PRODUCTS\"** and select the **ACCOUNT INFORMATION - UK OPEN BANKING API**    6. Click **\\\"START USING THIS API\\\"**, choose your app and click  **\"SUBSCRIBE\"**    7. Get an Access Token using the Access Token Flow and the API scopes provided in the Authentication and Authorization (OAuth2) section below    8. Create a Sandbox    9. Play with the API       ### Sandbox Flow    The Sandbox Flow matches the Production Flow. The difference lies into the Data used. Instead of live  data, the Sandbox flow uses mocked data.      ### Production Flow      The Production Flow is described in the [UK Open Banking v3.1.5  Specification](https://openbankinguk.github.io/read-write-api-site3/v3.1.5/profiles/account-and-transaction-api-profile.html)    More details about the implementation specifics followed, please visit section **UK OPB Implementation  Specifics**      ## Authentication and Authorization (OAuth2)    This API version uses the OAuth2 protocol for authentication and authorization, which means that a  Bearer (access token) should be acquired. An access token can be retrieved using the client_id and  client_secret of the APP that you created and subscribed in this API, and your own credentials  (username, password) that you use to sign in the NBG Technology HUB. The scopes are defined below:    **Authorization Endpoint:**        https://my.nbg.gr/identity/connect/authorize      **Token Endpoint:**        https://my.nbg.gr/identity/connect/token    ### Authorization Code ###    **Sandbox Scopes:**        sandbox-uk-account-info-api-v1 offline_access      **Production Scopes:**        accounts offline_access    ### Client Credentials ###    **Sandbox Scopes:**        sandbox-uk-account-info-api-v1      **Production Scopes:**        accounts      See more [here](https://developer.nbg.gr/oauth-document)    ## QWAC Certificates    TPPs are required to present a QWAC certificate during API consumption. The API checks that this certificate has been provided and is valid. In sandbox mode the certificate validations are optional. To validate your certificate in sandbox implementation, please send us your QWAC certificate at developer@nbg.gr and set the HTTP Header **\\\"x-sandbox-qwac-certificate-check\\\"** with the value **\\\"true\\\"** in your requests.     ## SMS Challenge (One Time Password)    In order to successfully authorize an Accounts Access you will need to provide the SMS OTP (One Time Password) in the corresponding Accounts Consent UI Screen.    By default the SMS OTP will be sent to the mobile number declared upon singing up in the NBG Technology HUB.         ## Create your Sandbox    Create a new Sandbox application by invoking the POST /sandbox. This call will generate a new Sandbox  with a unique sandbox-id.      __Important!__ Before proceeding save the sandbox id you just created.      When you create a sandbox, users and sandbox specific data are generated as sample data.      ## Start Testing    Once you have your sandbox-id, you can start invoking the rest of the operations by providing the  mandatory http header **sandbox-id**  and the http headers described below.      ## Important notes      **Request headers**      The following HTTP header parameters are required for every call:      1. Authorization. The Auth2 Token    2. sandbox-id. Your Sandbox ID      **Consent**      In order to be able to effectively start using the Endpoints the appropriate Consent needs to be  created and set to the 'Authorised' status.       In order to create the Consent you need to at least set the required **permissions** and the **Risk**  sections.       Optionally you may set the       1. ExpirationDateTime. When the Consent expires       2. TransactionFromDateTime. Start Date to retrieve the transactions       3. TransactionToDateTime. End Date to retrieve the transactions     **Not Implemented Endpoints**    The following endpoints are not implemented in the API    1. GET /balances  2. GET /transactions  3. GET /beneficiaries  4. GET /accounts/\\{AccountId\\}/direct-debits  5. GET /direct-debits  6. GET /standing-orders  7. GET /accounts/\\{AccountId\\}/product  8. GET /products  9. GET /accounts/\\{AccountId\\}/offers  10. GET /offers  11. GET /scheduled-payments  12. GET /statements      ## Error Codes    The error codes and their description can be found  [here](https://openbankinguk.github.io/read-write-api-site3/v3.1.5/profiles/read-write-data-api-profile.html#error-response-structure)      # UK OPB Implementation Specifics     Below you may find more specific information &amp; limitations regarding the implementation followed in the Production API.      ## Token Endpoint Client Authentication    At this point the supported __Client Authentication__ method is \"__Client Secret Basic__\" - usage of \"Client ID\" &amp; \"Client Secret\".      ## Consent Authorization    For a PSU to Authorize a Consent, they need to be redirected to the appropriate Consent UI.    For this redirection to take place the TPP needs to follow the Authorization Endpoint by amending the generated \"Consent ID\", like this: https://my.nbg.gr/identity/connect/authorize?consent_id={{consent_id}}&amp;client_id={{client_id}}&amp;scope={{scope}}&amp;redirect_uri={{redirect_uri}}&amp;response_type=code    Once the PSU is redirected to the Consent Authorization Screen, they need to enter their IBank (Production) or Developer Portal (Sandbox) Credentials and either Authorize or Reject the Consent.    At this point the Consent is binded with the PSU.      ## Debtor Account  Currently, only the \"UK.OBIE.IBAN\" scheme is supported.        # Feedback and Questions    We would love to hear your feedback and answer your questions. Send us at  [developer@nbg.gr](developer@nbg.gr)      Check out our [Sandbox Postman  Collection](https://github.com/NBG-Developer-Portal/Account-Information-UK-Open-Banking)!      ________________________________________    Created by [**NBG**](https://www.nbg.gr/).   # Entities    Below, the main entities are documented.  &lt;a name=OBExternalPermissions1Code&gt;&lt;/a&gt;  ## OBExternalPermissions1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;ReadAccountsBasic&lt;/li&gt;&lt;li&gt;ReadAccountsDetail&lt;/li&gt;&lt;li&gt;ReadBalances&lt;/li&gt;&lt;li&gt;ReadBeneficiariesBasic&lt;/li&gt;&lt;li&gt;ReadBeneficiariesDetail&lt;/li&gt;&lt;li&gt;ReadDirectDebits&lt;/li&gt;&lt;li&gt;ReadOffers&lt;/li&gt;&lt;li&gt;ReadPAN&lt;/li&gt;&lt;li&gt;ReadParty&lt;/li&gt;&lt;li&gt;ReadPartyPSU&lt;/li&gt;&lt;li&gt;ReadProducts&lt;/li&gt;&lt;li&gt;ReadScheduledPaymentsBasic&lt;/li&gt;&lt;li&gt;ReadScheduledPaymentsDetail&lt;/li&gt;&lt;li&gt;ReadStandingOrdersBasic&lt;/li&gt;&lt;li&gt;ReadStandingOrdersDetail&lt;/li&gt;&lt;li&gt;ReadStatementsBasic&lt;/li&gt;&lt;li&gt;ReadStatementsDetail&lt;/li&gt;&lt;li&gt;ReadTransactionsBasic&lt;/li&gt;&lt;li&gt;ReadTransactionsCredits&lt;/li&gt;&lt;li&gt;ReadTransactionsDebits&lt;/li&gt;&lt;li&gt;ReadTransactionsDetail&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBReadData1&gt;&lt;/a&gt;  ## OBReadData1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Permissions| Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP.| array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]| | ExpirationDateTime| Specified date and time the permissions will expire. If this is not populated, the permissions will be open ended. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionFromDateTime| Specified start date and time for the transaction query period. If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionToDateTime| Specified end date and time for the transaction query period. If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=OBRisk2&gt;&lt;/a&gt;  ## OBRisk2  The Risk section is sent by the initiating party to the ASPSP. It is used to specify additional details for risk scoring for Account Info.   ### Attributes   | Name| Description| Values| | -----| -----| -----|   &lt;a name=OBReadConsent1&gt;&lt;/a&gt;  ## OBReadConsent1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadData1](#OBReadData1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Permissions [array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]]&lt;/li&gt; &lt;li&gt;ExpirationDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionFromDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionToDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Risk | Entity | &lt;details&gt;&lt;summary&gt;[OBRisk2](#OBRisk2)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |    &lt;a name=ErrorCode&gt;&lt;/a&gt;  ## ErrorCode  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| This is Data Type gives a low level textual error code to help categorise an error response. The applicable HTTP response code is also given.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;UK.OBIE.Field.Expected&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.Invalid&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.InvalidDate&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.Missing&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.Unexpected&lt;/li&gt;&lt;li&gt;UK.OBIE.Header.Invalid&lt;/li&gt;&lt;li&gt;UK.OBIE.Header.Missing&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.ConsentMismatch&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.InvalidConsentStatus&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.InvalidFormat&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.NotFound&lt;/li&gt;&lt;li&gt;UK.OBIE.Rules.AfterCutOffDateTime&lt;/li&gt;&lt;li&gt;UK.OBIE.Rules.DuplicateReference&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Invalid&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.InvalidClaim&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.MissingClaim&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Malformed&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Missing&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Unexpected&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.AccountIdentifier&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.AccountSecondaryIdentifier&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.Currency&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.EventType&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.Frequency&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.LocalInstrument&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.Scheme&lt;/li&gt;&lt;li&gt;UK.OBIE.Reauthenticate&lt;/li&gt;&lt;li&gt;UK.OBIE.Rules.ResourceAlreadyExists&lt;/li&gt;&lt;li&gt;UK.OBIE.UnexpectedError&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBError1&gt;&lt;/a&gt;  ## OBError1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | ErrorCode | Entity | &lt;details&gt;&lt;summary&gt;[ErrorCode](#ErrorCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Message| A description of the error that occurred. e.g., 'A mandatory field isn't supplied' or 'RequestedExecutionDateTime must be in future'OBIE doesn't standardise this field| string| | Path| Recommended but optional reference to the JSON Path of the field with error, e.g., Data.Initiation.InstructedAmount.Currency| string|   &lt;a name=OBErrorResponse1&gt;&lt;/a&gt;  ## OBErrorResponse1  An array of detail error codes, and messages, and URLs to documentation to help remediation.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | Code| High level textual error code, to help categorize the errors.| string| | Id| A unique reference for the error instance, for audit purposes, in case of unknown/unclassified errors.| string| | Message| Brief Error message, e.g., 'There is something wrong with the request parameters provided'| string| | Errors| Gets or Sets Errors| array[[OBError1](#OBError1)]|   &lt;a name=OBExternalRequestStatus1Code&gt;&lt;/a&gt;  ## OBExternalRequestStatus1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| Specifies the status of consent resource in code form.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Authorised&lt;/li&gt;&lt;li&gt;AwaitingAuthorisation&lt;/li&gt;&lt;li&gt;Rejected&lt;/li&gt;&lt;li&gt;Revoked&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBReadDataConsentResponse1&gt;&lt;/a&gt;  ## OBReadDataConsentResponse1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | ConsentId| Unique identification as assigned to identify the account access consent resource.| string| | CreationDateTime| Date and time at which the resource was created. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Status | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalRequestStatus1Code](#OBExternalRequestStatus1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | StatusUpdateDateTime| Date and time at which the resource status was updated. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Permissions| Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP.| array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]| | ExpirationDateTime| Specified date and time the permissions will expire. If this is not populated, the permissions will be open ended. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionFromDateTime| Specified start date and time for the transaction query period. If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionToDateTime| Specified end date and time for the transaction query period. If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=Links&gt;&lt;/a&gt;  ## Links  Links relevant to the payload   ### Attributes   | Name| Description| Values| | -----| -----| -----| | Self| -| string| | First| -| string| | Prev| -| string| | Next| -| string| | Last| -| string|   &lt;a name=Meta&gt;&lt;/a&gt;  ## Meta  Meta Data relevant to the payload   ### Attributes   | Name| Description| Values| | -----| -----| -----| | TotalPages| -| integer| | FirstAvailableDateTime| All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | LastAvailableDateTime| All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=OBReadConsentResponse1&gt;&lt;/a&gt;  ## OBReadConsentResponse1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataConsentResponse1](#OBReadDataConsentResponse1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;ConsentId [string]&lt;/li&gt; &lt;li&gt;CreationDateTime [string]&lt;/li&gt; &lt;li&gt;&lt;details&gt;&lt;summary&gt;Status [[OBExternalRequestStatus1Code](#OBExternalRequestStatus1Code)]&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;li&gt;StatusUpdateDateTime [string]&lt;/li&gt; &lt;li&gt;Permissions [array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]]&lt;/li&gt; &lt;li&gt;ExpirationDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionFromDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionToDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Risk | Entity | &lt;details&gt;&lt;summary&gt;[OBRisk2](#OBRisk2)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBExternalAccountType1Code&gt;&lt;/a&gt;  ## OBExternalAccountType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Business&lt;/li&gt;&lt;li&gt;Personal&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBExternalAccountSubType1Code&gt;&lt;/a&gt;  ## OBExternalAccountSubType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;ChargeCard&lt;/li&gt;&lt;li&gt;CreditCard&lt;/li&gt;&lt;li&gt;CurrentAccount&lt;/li&gt;&lt;li&gt;EMoney&lt;/li&gt;&lt;li&gt;Loan&lt;/li&gt;&lt;li&gt;Mortgage&lt;/li&gt;&lt;li&gt;PrePaidCard&lt;/li&gt;&lt;li&gt;Savings&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBCashAccount5&gt;&lt;/a&gt;  ## OBCashAccount5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | SchemeName| Name of the identification scheme, in a coded form as published in an external list.| string| | Identification| Identification assigned by an institution to identify an account. This identification is known by the account owner.| string| | Name| The account name is the name or names of the account owner(s) represented at an account level, as displayed by the ASPSP's online channels. Note, the account name is not the product name or the nickname of the account.| string| | SecondaryIdentification| This is secondary identification of the account, as assigned by the account servicing institution. This can be used by building societies to additionally identify accounts with a roll number(in addition to a sort code and account number combination).| string|   &lt;a name=OBBranchAndFinancialInstitutionIdentification5&gt;&lt;/a&gt;  ## OBBranchAndFinancialInstitutionIdentification5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | SchemeName| Name of the identification scheme, in a coded form as published in an external list.| string| | Identification| Unique and unambiguous identification of the servicing institution.| string|   &lt;a name=OBAccount6&gt;&lt;/a&gt;  ## OBAccount6  Unambiguous identification of the account to which credit and debit entries are made.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | Currency| Identification of the currency in which the account is held.  Usage: Currency should only be used in case one and the same account number covers several currencies and the initiating party needs to identify which currency needs to be used for settlement on the account.| string| | AccountType | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalAccountType1Code](#OBExternalAccountType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | AccountSubType | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalAccountSubType1Code](#OBExternalAccountSubType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Description| Specifies the description of the account type.| string| | Nickname| The nickname of the account, assigned by the account owner in order to provide an additional means of identification of the account.| string| | OpeningDate| Date on which the account and related basic services are effectively operational for the account owner.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Account| Provides the details to identify an account.| array[[OBCashAccount5](#OBCashAccount5)]| | Servicer | Entity | &lt;details&gt;&lt;summary&gt;[OBBranchAndFinancialInstitutionIdentification5](#OBBranchAndFinancialInstitutionIdentification5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataAccount5&gt;&lt;/a&gt;  ## OBReadDataAccount5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Account| Unambiguous identification of the account to which credit and debit entries are made.| array[[OBAccount6](#OBAccount6)]|   &lt;a name=OBReadAccount5&gt;&lt;/a&gt;  ## OBReadAccount5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataAccount5](#OBReadDataAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Account [array[[OBAccount6](#OBAccount6)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBCreditDebitCode&gt;&lt;/a&gt;  ## OBCreditDebitCode  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Credit&lt;/li&gt;&lt;li&gt;Debit&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBBalanceType1Code&gt;&lt;/a&gt;  ## OBBalanceType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;ClosingAvailable&lt;/li&gt;&lt;li&gt;ClosingBooked&lt;/li&gt;&lt;li&gt;ClosingCleared&lt;/li&gt;&lt;li&gt;Expected&lt;/li&gt;&lt;li&gt;ForwardAvailable&lt;/li&gt;&lt;li&gt;Information&lt;/li&gt;&lt;li&gt;InterimAvailable&lt;/li&gt;&lt;li&gt;InterimBooked&lt;/li&gt;&lt;li&gt;InterimCleared&lt;/li&gt;&lt;li&gt;OpeningAvailable&lt;/li&gt;&lt;li&gt;OpeningBooked&lt;/li&gt;&lt;li&gt;OpeningCleared&lt;/li&gt;&lt;li&gt;PreviouslyClosedBooked&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBActiveOrHistoricCurrencyAndAmount&gt;&lt;/a&gt;  ## OBActiveOrHistoricCurrencyAndAmount    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Amount| A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217.| string| | Currency| A code allocated to a currency by a Maintenance Agency under an international identification scheme, as described in the latest edition of the international standard ISO 4217 \"Codes for the representation of currencies and funds\".| string|   &lt;a name=OBExternalLimitType1Code&gt;&lt;/a&gt;  ## OBExternalLimitType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Available&lt;/li&gt;&lt;li&gt;Credit&lt;/li&gt;&lt;li&gt;Emergency&lt;/li&gt;&lt;li&gt;Pre-Agreed&lt;/li&gt;&lt;li&gt;Temporary&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBCreditLine1&gt;&lt;/a&gt;  ## OBCreditLine1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Included| Indicates whether or not the credit line is included in the balance of the account. Usage: If not present, credit line is not included in the balance amount of the account.| boolean| | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalLimitType1Code](#OBExternalLimitType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBCashBalance1&gt;&lt;/a&gt;  ## OBCashBalance1  Set of elements used to define the balance details.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | CreditDebitIndicator | Entity | &lt;details&gt;&lt;summary&gt;[OBCreditDebitCode](#OBCreditDebitCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBBalanceType1Code](#OBBalanceType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | DateTime| Indicates the date (and time) of the balance.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | CreditLine| Set of elements used to provide details on the credit line.| array[[OBCreditLine1](#OBCreditLine1)]|   &lt;a name=OBReadDataBalance1&gt;&lt;/a&gt;  ## OBReadDataBalance1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Balance| Set of elements used to define the balance details.| array[[OBCashBalance1](#OBCashBalance1)]|   &lt;a name=OBReadBalance1&gt;&lt;/a&gt;  ## OBReadBalance1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataBalance1](#OBReadDataBalance1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Balance [array[[OBCashBalance1](#OBCashBalance1)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBBeneficiaryType1Code&gt;&lt;/a&gt;  ## OBBeneficiaryType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| Specifies the Beneficiary Type.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Trusted&lt;/li&gt;&lt;li&gt;Ordinary&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBBeneficiary5&gt;&lt;/a&gt;  ## OBBeneficiary5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | BeneficiaryType | Entity | &lt;details&gt;&lt;summary&gt;[OBBeneficiaryType1Code](#OBBeneficiaryType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount5](#OBCashAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;li&gt;SecondaryIdentification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataBeneficiary5&gt;&lt;/a&gt;  ## OBReadDataBeneficiary5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Beneficiary| -| array[[OBBeneficiary5](#OBBeneficiary5)]|   &lt;a name=OBReadBeneficiary5&gt;&lt;/a&gt;  ## OBReadBeneficiary5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataBeneficiary5](#OBReadDataBeneficiary5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Beneficiary [array[[OBBeneficiary5](#OBBeneficiary5)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBParty2&gt;&lt;/a&gt;  ## OBParty2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | PartyId| A unique and immutable identifier used to identify the customer resource. This identifier has no meaning to the account owner.| string| | Name| Name by which a party is known and which is usually used to identify that party.| string|   &lt;a name=OBReadDataParty2&gt;&lt;/a&gt;  ## OBReadDataParty2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Party | Entity | &lt;details&gt;&lt;summary&gt;[OBParty2](#OBParty2)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;PartyId [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadParty2&gt;&lt;/a&gt;  ## OBReadParty2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataParty2](#OBReadDataParty2)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;Party [[OBParty2](#OBParty2)]&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;PartyId [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataParty3&gt;&lt;/a&gt;  ## OBReadDataParty3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Party| -| array[[OBParty2](#OBParty2)]|   &lt;a name=OBReadParty3&gt;&lt;/a&gt;  ## OBReadParty3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataParty3](#OBReadDataParty3)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Party [array[[OBParty2](#OBParty2)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=SandboxRequest&gt;&lt;/a&gt;  ## SandboxRequest  Request to create a new sandbox   ### Attributes   | Name| Description| Values| | -----| -----| -----| | sandboxId| Sandbox Id| string|   &lt;a name=ErrorResponse&gt;&lt;/a&gt;  ## ErrorResponse    ### Attributes   | Name| Description| Values| | -----| -----| -----| | errorMessage| -| string|   &lt;a name=SandboxRetryCacheEntry&gt;&lt;/a&gt;  ## SandboxRetryCacheEntry  Keeps the number of calls without x-fapi-customer-ip-address header present   ### Attributes   | Name| Description| Values| | -----| -----| -----| | cacheKey| Cache key| string| | count| Number of retries ( up to 4 )| integer| | expirationTimestamp| Expiration timestamp of the entry| string|   &lt;a name=SandboxBankAccountInfo&gt;&lt;/a&gt;  ## SandboxBankAccountInfo  General account information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | currency| Currency (EUR, USD ...)| string| | iban| Account's IBAN| string| | accountType| Account's type (Business, Personal)| string| | accountSubType| Account's sub-type (ChargeCard, CreditCard, CurrentAccount ...)| string| | description| Account's description| string| | alias| Account's alias| string| | openingDate| Account's opening date| string| | availableBalance| Account's available balance| number| | ledgerBalance| Account's ledger balance| number| | overdraftLimit| Account's overdraft limit| number|   &lt;a name=SandboxParty&gt;&lt;/a&gt;  ## SandboxParty  Connected party information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | id| Party id| string| | name| Name| string|   &lt;a name=SandboxBeneficiary&gt;&lt;/a&gt;  ## SandboxBeneficiary  Beneficiary information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | name| Beneficiary name| string|   &lt;a name=SandboxStandingOrder&gt;&lt;/a&gt;  ## SandboxStandingOrder  Standing order information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | description| Standing order short description| string| | frequency| Standing order frequency| string| | firstPaymentDate| Standing order first collection date| string| | nextPaymentDate| Standing order next collection date| string| | finalPaymentDate| Standing order final collection date| string| | lastPaymentDate| Standing order last executed payment date| string| | status| Standing order status (Active, Inactive)| string| | amount| Standing order amount| number|   &lt;a name=SandboxScheduledPayment&gt;&lt;/a&gt;  ## SandboxScheduledPayment  Scheduled payment information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | description| Scheduled payment's short description| string| | executionDate| Scheduled payment's execution date| string| | amount| Amount| number| | senderReference| Debtor / Sender reference| string|   &lt;a name=SandboxStatement&gt;&lt;/a&gt;  ## SandboxStatement  Statement information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | number| Statement number| string| | year| Statement year| integer| | month| Statement month| integer|   &lt;a name=SandboxTransaction&gt;&lt;/a&gt;  ## SandboxTransaction  Transaction information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | reference| Transaction reference| string| | amount| Amount| number| | currency| Currency (EUR, USD ...)| string| | creditDebit| Credit / Debit indicator| string| | valueDateTime| Valeur| string| | bookingDateTime| Booking date time| string| | description| Description| string| | accountingBalance| Balance| number| | relatedAccount| Related account| string| | relatedName| Related account| string| | transactionCode| Transaction code| string|   &lt;a name=SandboxBankAccount&gt;&lt;/a&gt;  ## SandboxBankAccount  Sandbox bank account   ### Attributes   | Name| Description| Values| | -----| -----| -----| | info | Entity | &lt;details&gt;&lt;summary&gt;[SandboxBankAccountInfo](#SandboxBankAccountInfo)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;currency [string]&lt;/li&gt; &lt;li&gt;iban [string]&lt;/li&gt; &lt;li&gt;accountType [string]&lt;/li&gt; &lt;li&gt;accountSubType [string]&lt;/li&gt; &lt;li&gt;description [string]&lt;/li&gt; &lt;li&gt;alias [string]&lt;/li&gt; &lt;li&gt;openingDate [string]&lt;/li&gt; &lt;li&gt;availableBalance [number]&lt;/li&gt; &lt;li&gt;ledgerBalance [number]&lt;/li&gt; &lt;li&gt;overdraftLimit [number]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | party | Entity | &lt;details&gt;&lt;summary&gt;[SandboxParty](#SandboxParty)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;id [string]&lt;/li&gt; &lt;li&gt;name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | beneficiaries| List of account's beneficiaries| array[[SandboxBeneficiary](#SandboxBeneficiary)]| | standingOrders| List of account's standing orders| array[[SandboxStandingOrder](#SandboxStandingOrder)]| | scheduledPayments| List of account's scheduled payments| array[[SandboxScheduledPayment](#SandboxScheduledPayment)]| | statements| List of account's statements| array[[SandboxStatement](#SandboxStatement)]| | transactions| List of account's transactions| array[[SandboxTransaction](#SandboxTransaction)]|   &lt;a name=SandboxCardInfo&gt;&lt;/a&gt;  ## SandboxCardInfo  Sandbox card information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | number| Card number| string| | description| Description| string| | holderName| Holder name| string| | expiration| Expiration date (05/2022)| string| | type| Type| string| | subType| Sub type| string| | availableBalance| Available balance| number| | ledgerBalance| Ledger balance| number| | creditLimit| Credit limit ( applicable to credit cards )| number|   &lt;a name=SandboxCard&gt;&lt;/a&gt;  ## SandboxCard  Sandbox card   ### Attributes   | Name| Description| Values| | -----| -----| -----| | info | Entity | &lt;details&gt;&lt;summary&gt;[SandboxCardInfo](#SandboxCardInfo)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;number [string]&lt;/li&gt; &lt;li&gt;description [string]&lt;/li&gt; &lt;li&gt;holderName [string]&lt;/li&gt; &lt;li&gt;expiration [string]&lt;/li&gt; &lt;li&gt;type [string]&lt;/li&gt; &lt;li&gt;subType [string]&lt;/li&gt; &lt;li&gt;availableBalance [number]&lt;/li&gt; &lt;li&gt;ledgerBalance [number]&lt;/li&gt; &lt;li&gt;creditLimit [number]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | party | Entity | &lt;details&gt;&lt;summary&gt;[SandboxParty](#SandboxParty)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;id [string]&lt;/li&gt; &lt;li&gt;name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | statements| Card statements| array[[SandboxStatement](#SandboxStatement)]| | transactions| Card transactions| array[[SandboxTransaction](#SandboxTransaction)]|   &lt;a name=SandboxUser&gt;&lt;/a&gt;  ## SandboxUser  User data   ### Attributes   | Name| Description| Values| | -----| -----| -----| | userId| Connected user id| string| | retryCacheEntries| Retry cache entries| array[[SandboxRetryCacheEntry](#SandboxRetryCacheEntry)]| | accounts| List of accounts| array[[SandboxBankAccount](#SandboxBankAccount)]| | cards| List of cards| array[[SandboxCard](#SandboxCard)]|   &lt;a name=Sandbox&gt;&lt;/a&gt;  ## Sandbox  Sandbox model   ### Attributes   | Name| Description| Values| | -----| -----| -----| | sandboxId| Sandbox id| string| | users| List of users| array[[SandboxUser](#SandboxUser)]|   &lt;a name=OBExternalScheduleType1Code&gt;&lt;/a&gt;  ## OBExternalScheduleType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Arrival&lt;/li&gt;&lt;li&gt;Execution&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBScheduledPayment3&gt;&lt;/a&gt;  ## OBScheduledPayment3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | ScheduledPaymentId| A unique and immutable identifier used to identify the scheduled payment resource. This identifier has no meaning to the account owner.| string| | ScheduledPaymentDateTime| The date on which the scheduled payment will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | ScheduledType | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalScheduleType1Code](#OBExternalScheduleType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Reference| Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. Usage: If available, the initiating party should provide this reference in the structured remittance information, to enable reconciliation by the creditor upon receipt of the amount of money. If the business context requires the use of a creditor reference or a payment remit identification, and only one identifier can be passed through the end-to-end chain, the creditor's reference or payment remittance identification should be quoted in the end-to-end transaction identification.| string| | DebtorReference| A reference value provided by the PSU to the PISP while setting up the scheduled payment.| string| | InstructedAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount5](#OBCashAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;li&gt;SecondaryIdentification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataScheduledPayment3&gt;&lt;/a&gt;  ## OBReadDataScheduledPayment3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | ScheduledPayment| -| array[[OBScheduledPayment3](#OBScheduledPayment3)]|   &lt;a name=OBReadScheduledPayment3&gt;&lt;/a&gt;  ## OBReadScheduledPayment3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataScheduledPayment3](#OBReadDataScheduledPayment3)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;ScheduledPayment [array[[OBScheduledPayment3](#OBScheduledPayment3)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBExternalStandingOrderStatus1Code&gt;&lt;/a&gt;  ## OBExternalStandingOrderStatus1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Active&lt;/li&gt;&lt;li&gt;Inactive&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBStandingOrder5&gt;&lt;/a&gt;  ## OBStandingOrder5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | StandingOrderId| A unique and immutable identifier used to identify the standing order resource. This identifier has no meaning to the account owner.| string| | Frequency| Individual Definitions: IntrvlMnthDay - An interval specified in months(between 01, 02, 03, 04, 06, 12, 24), specifying the day within the month(01 to 31) Full Regular Expression: ^(IntrvlMnthDay:(0[1,2,3,4,6]|12|24):(0[1-9]|[12] [0-9]|3[01]))$| string| | Reference| Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. Usage: If available, the initiating party should provide this reference in the structured remittance information, to enable reconciliation by the creditor upon receipt of the amount of money. If the business context requires the use of a creditor reference or a payment remit identification, and only one identifier can be passed through the end-to-end chain, the creditor's reference or payment remittance identification should be quoted in the end-to-end transaction identification.| string| | FirstPaymentDateTime| The date on which the first payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | NextPaymentDateTime| The date on which the next payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | LastPaymentDateTime| The date on which the last (most recent) payment for a Standing Order schedule was made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | FinalPaymentDateTime| The date on which the final payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | StandingOrderStatusCode | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalStandingOrderStatus1Code](#OBExternalStandingOrderStatus1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | FirstPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | NextPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | LastPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | FinalPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount5](#OBCashAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;li&gt;SecondaryIdentification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataStandingOrder5&gt;&lt;/a&gt;  ## OBReadDataStandingOrder5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | StandingOrder| -| array[[OBStandingOrder5](#OBStandingOrder5)]|   &lt;a name=OBReadStandingOrder6&gt;&lt;/a&gt;  ## OBReadStandingOrder6    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataStandingOrder5](#OBReadDataStandingOrder5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;StandingOrder [array[[OBStandingOrder5](#OBStandingOrder5)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBExternalStatementType1Code&gt;&lt;/a&gt;  ## OBExternalStatementType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;AccountClosure&lt;/li&gt;&lt;li&gt;AccountOpening&lt;/li&gt;&lt;li&gt;Annual&lt;/li&gt;&lt;li&gt;Interim&lt;/li&gt;&lt;li&gt;RegularPeriodic&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBStatement2&gt;&lt;/a&gt;  ## OBStatement2  Provides further details on a statement resource.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | StatementId| Unique identifier for the statement resource within an servicing institution. This identifier is both unique and immutable.| string| | StatementReference| Unique reference for the statement. This reference may be optionally populated if available.| string| | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalStatementType1Code](#OBExternalStatementType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | StartDateTime| Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | EndDateTime| Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | CreationDateTime| Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=OBReadDataStatement2&gt;&lt;/a&gt;  ## OBReadDataStatement2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Statement| Provides further details on a statement resource.| array[[OBStatement2](#OBStatement2)]|   &lt;a name=OBReadStatement2&gt;&lt;/a&gt;  ## OBReadStatement2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataStatement2](#OBReadDataStatement2)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Statement [array[[OBStatement2](#OBStatement2)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBEntryStatus1Code&gt;&lt;/a&gt;  ## OBEntryStatus1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Booked&lt;/li&gt;&lt;li&gt;Pending&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=ProprietaryBankTransactionCodeStructure1&gt;&lt;/a&gt;  ## ProprietaryBankTransactionCodeStructure1  Set of elements to fully identify a proprietary bank transaction code.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | Code| Proprietary bank transaction code to identify the underlying transaction.| string| | Issuer| Identification of the issuer of the proprietary bank transaction code.| string|   &lt;a name=OBTransactionCashBalance&gt;&lt;/a&gt;  ## OBTransactionCashBalance  Set of elements used to define the balance as a numerical representation of the net increases and decreases in an account after a transaction entry is applied to the account.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | CreditDebitIndicator | Entity | &lt;details&gt;&lt;summary&gt;[OBCreditDebitCode](#OBCreditDebitCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBBalanceType1Code](#OBBalanceType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBCashAccount6&gt;&lt;/a&gt;  ## OBCashAccount6  Unambiguous identification of the account of the creditor, in the case of a debit transaction.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | SchemeName| Name of the identification scheme, in a coded form as published in an external list.| string| | Identification| Identification assigned by an institution to identify an account. This identification is known by the account owner.| string| | Name| The account name is the name or names of the account owner(s) represented at an account level, as displayed by the ASPSP's online channels. Note, the account name is not the product name or the nickname of the account.| string|   &lt;a name=OBTransaction6&gt;&lt;/a&gt;  ## OBTransaction6  Provides further details on an entry in the report.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | TransactionReference| Unique reference for the transaction. This reference is optionally populated, and may as an example be the FPID in the Faster Payments context.| string| | CreditDebitIndicator | Entity | &lt;details&gt;&lt;summary&gt;[OBCreditDebitCode](#OBCreditDebitCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Status | Entity | &lt;details&gt;&lt;summary&gt;[OBEntryStatus1Code](#OBEntryStatus1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | BookingDateTime| Date and time when a transaction entry is posted to an account on the account servicer's books. Usage: Booking date is the expected booking date, unless the status is booked, in which case it is the actual booking date.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | ValueDateTime| Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit transaction entry. Usage: If transaction entry status is pending and value date is present, then the value date refers to an expected/requested value date. For transaction entries subject to availability/float and for which availability information is provided, the value date must not be used.In this case the availability component identifies the number of availability days.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionInformation| Further details of the transaction. This is the transaction narrative, which is unstructured text.| string| | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | ProprietaryBankTransactionCode | Entity | &lt;details&gt;&lt;summary&gt;[ProprietaryBankTransactionCodeStructure1](#ProprietaryBankTransactionCodeStructure1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Code [string]&lt;/li&gt; &lt;li&gt;Issuer [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Balance | Entity | &lt;details&gt;&lt;summary&gt;[OBTransactionCashBalance](#OBTransactionCashBalance)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;CreditDebitIndicator [[OBCreditDebitCode](#OBCreditDebitCode)]&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;Type [[OBBalanceType1Code](#OBBalanceType1Code)]&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;Amount [[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)]&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount6](#OBCashAccount6)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | DebtorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount6](#OBCashAccount6)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataTransaction6&gt;&lt;/a&gt;  ## OBReadDataTransaction6    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Transaction| Provides further details on an entry in the report.| array[[OBTransaction6](#OBTransaction6)]|   &lt;a name=OBReadTransaction6&gt;&lt;/a&gt;  ## OBReadTransaction6    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataTransaction6](#OBReadDataTransaction6)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Transaction [array[[OBTransaction6](#OBTransaction6)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |   # Authentication  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;
 *
 * The version of the OpenAPI document: v3.1.5
 * Contact: developer@nbg.gr
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
import org.apache.oltu.oauth2.client.request.OAuthClientRequest.TokenRequestBuilder;
import org.apache.oltu.oauth2.common.message.types.GrantType;

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
import org.openapitools.client.auth.OAuth;
import org.openapitools.client.auth.RetryingOAuth;
import org.openapitools.client.auth.OAuthFlow;

/**
 * <p>ApiClient class.</p>
 */
public class ApiClient {

    private String basePath = "https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5";
    protected List<ServerConfiguration> servers = new ArrayList<ServerConfiguration>(Arrays.asList(
    new ServerConfiguration(
      "https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5",
      "Sandbox Server",
      new HashMap<String, ServerVariable>()
    ),
    new ServerConfiguration(
      "https://services.nbg.gr/apis/open-banking/v3.1.5/aisp",
      "Production Server",
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
        authentications.put("Authorization-Code-Token", new OAuth());
        authentications.put("Client-Credentials-Token", new OAuth());
        authentications.put("Client-Id", new ApiKeyAuth("header", "Client-Id"));
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
        authentications.put("Authorization-Code-Token", new OAuth());
        authentications.put("Client-Credentials-Token", new OAuth());
        authentications.put("Client-Id", new ApiKeyAuth("header", "Client-Id"));
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with client ID
     *
     * @param clientId client ID
     */
    public ApiClient(String clientId) {
        this(clientId, null, null);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with client ID and additional parameters
     *
     * @param clientId client ID
     * @param parameters a {@link java.util.Map} of parameters
     */
    public ApiClient(String clientId, Map<String, String> parameters) {
        this(clientId, null, parameters);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with client ID, secret, and additional parameters
     *
     * @param clientId client ID
     * @param clientSecret client secret
     * @param parameters a {@link java.util.Map} of parameters
     */
    public ApiClient(String clientId, String clientSecret, Map<String, String> parameters) {
        this(null, clientId, clientSecret, parameters);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with base path, client ID, secret, and additional parameters
     *
     * @param basePath base path
     * @param clientId client ID
     * @param clientSecret client secret
     * @param parameters a {@link java.util.Map} of parameters
     */
    public ApiClient(String basePath, String clientId, String clientSecret, Map<String, String> parameters) {
        init();
        if (basePath != null) {
            this.basePath = basePath;
        }

        String tokenUrl = "https://my.nbg.gr/identity/connect/token";
        if (!"".equals(tokenUrl) && !URI.create(tokenUrl).isAbsolute()) {
            URI uri = URI.create(getBasePath());
            tokenUrl = uri.getScheme() + ":" +
                (uri.getAuthority() != null ? "//" + uri.getAuthority() : "") +
                tokenUrl;
            if (!URI.create(tokenUrl).isAbsolute()) {
                throw new IllegalArgumentException("OAuth2 token URL must be an absolute URL");
            }
        }
        RetryingOAuth retryingOAuth = new RetryingOAuth(tokenUrl, clientId, OAuthFlow.ACCESS_CODE, clientSecret, parameters);
        authentications.put(
                "Authorization-Code-Token",
                retryingOAuth
        );
        initHttpClient(Collections.<Interceptor>singletonList(retryingOAuth));
        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("Client-Id", new ApiKeyAuth("header", "Client-Id"));

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
        setUserAgent("OpenAPI-Generator/v3.1.5/java");

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
     * @param basePath Base path of the URL (e.g https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5
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
        for (Authentication auth : authentications.values()) {
            if (auth instanceof OAuth) {
                ((OAuth) auth).setAccessToken(accessToken);
                return;
            }
        }
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
     * Helper method to configure the token endpoint of the first oauth found in the apiAuthorizations (there should be only one)
     *
     * @return Token request builder
     */
    public TokenRequestBuilder getTokenEndPoint() {
        for (Authentication apiAuth : authentications.values()) {
            if (apiAuth instanceof RetryingOAuth) {
                RetryingOAuth retryingOAuth = (RetryingOAuth) apiAuth;
                return retryingOAuth.getTokenRequestBuilder();
            }
        }
        return null;
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
