/**
 * Account and Transaction API Specification - UK
 * ## Functionality at a glance    The NBG \"UK OPB - Account and Transaction v3.1.5\" API follows the [UK Open Banking Specification      v3.1.5](https://openbankinguk.github.io/read-write-api-site3/v3.1.5/profiles/account-and-transaction-api-profile.html)    This Account and Transaction API Specification describes the flows and payloads for retrieving a list of accounts and their transactions.    The API endpoints described here allow a AISP to:      * Create the Consent with the appropriate permissions in order to be able to access the API Endpoints    * Retrieve the list of accounts    * Retrieve an account's details    * Retrieve an account's balances    * Retrieve an account's transactions    * Retrieve an account's beneficiaries    * Retrieve an account's standing orders    * Retrieve an account's party    * Retrieve an account's scheduled payments    * Retrieve an account's statements        ## Quick Getting Started      1. **Login/Register** to the NBG Technology HUB    2. Go to **\"APPS\"**    3. Select your Organization and go to step 4. If you want to create a new Organization click **\\\"CREATE AN ORGANIZATION\\\"** and follow the steps below:   1. Enter the title of your Organization   2. Enter a short description of your Organization (optional)   3. Click **\"SUBMIT\"**    4. Select the Organization of choice and click **\"ADD AN APPLICATION\"**      1. Fill in the forms (title and short description)     2. Check **\\\"Authorization Code\\\" and \\\"Client Credentials\\\"**      3. Enter the **OAuth Redirect and Post Logout URIs** (these are the URIs that we will redirect the user upon logging in and logging out respectively)            You can use the following redirect URL to easily test the API through the portal: *https://developer.nbg.gr/oauth2/redoc-callback*     4. Click **\"SUBMIT\"**     5. Store the APPs **\"Client ID\"** and **\"Client Secret\"**  5. Go to **\"API PRODUCTS\"** and select the **ACCOUNT INFORMATION - UK OPEN BANKING API**    6. Click **\\\"START USING THIS API\\\"**, choose your app and click  **\"SUBSCRIBE\"**    7. Get an Access Token using the Access Token Flow and the API scopes provided in the Authentication and Authorization (OAuth2) section below    8. Create a Sandbox    9. Play with the API       ### Sandbox Flow    The Sandbox Flow matches the Production Flow. The difference lies into the Data used. Instead of live  data, the Sandbox flow uses mocked data.      ### Production Flow      The Production Flow is described in the [UK Open Banking v3.1.5  Specification](https://openbankinguk.github.io/read-write-api-site3/v3.1.5/profiles/account-and-transaction-api-profile.html)    More details about the implementation specifics followed, please visit section **UK OPB Implementation  Specifics**      ## Authentication and Authorization (OAuth2)    This API version uses the OAuth2 protocol for authentication and authorization, which means that a  Bearer (access token) should be acquired. An access token can be retrieved using the client_id and  client_secret of the APP that you created and subscribed in this API, and your own credentials  (username, password) that you use to sign in the NBG Technology HUB. The scopes are defined below:    **Authorization Endpoint:**        https://my.nbg.gr/identity/connect/authorize      **Token Endpoint:**        https://my.nbg.gr/identity/connect/token    ### Authorization Code ###    **Sandbox Scopes:**        sandbox-uk-account-info-api-v1 offline_access      **Production Scopes:**        accounts offline_access    ### Client Credentials ###    **Sandbox Scopes:**        sandbox-uk-account-info-api-v1      **Production Scopes:**        accounts      See more [here](https://developer.nbg.gr/oauth-document)    ## QWAC Certificates    TPPs are required to present a QWAC certificate during API consumption. The API checks that this certificate has been provided and is valid. In sandbox mode the certificate validations are optional. To validate your certificate in sandbox implementation, please send us your QWAC certificate at developer@nbg.gr and set the HTTP Header **\\\"x-sandbox-qwac-certificate-check\\\"** with the value **\\\"true\\\"** in your requests.     ## SMS Challenge (One Time Password)    In order to successfully authorize an Accounts Access you will need to provide the SMS OTP (One Time Password) in the corresponding Accounts Consent UI Screen.    By default the SMS OTP will be sent to the mobile number declared upon singing up in the NBG Technology HUB.         ## Create your Sandbox    Create a new Sandbox application by invoking the POST /sandbox. This call will generate a new Sandbox  with a unique sandbox-id.      __Important!__ Before proceeding save the sandbox id you just created.      When you create a sandbox, users and sandbox specific data are generated as sample data.      ## Start Testing    Once you have your sandbox-id, you can start invoking the rest of the operations by providing the  mandatory http header **sandbox-id**  and the http headers described below.      ## Important notes      **Request headers**      The following HTTP header parameters are required for every call:      1. Authorization. The Auth2 Token    2. sandbox-id. Your Sandbox ID      **Consent**      In order to be able to effectively start using the Endpoints the appropriate Consent needs to be  created and set to the 'Authorised' status.       In order to create the Consent you need to at least set the required **permissions** and the **Risk**  sections.       Optionally you may set the       1. ExpirationDateTime. When the Consent expires       2. TransactionFromDateTime. Start Date to retrieve the transactions       3. TransactionToDateTime. End Date to retrieve the transactions     **Not Implemented Endpoints**    The following endpoints are not implemented in the API    1. GET /balances  2. GET /transactions  3. GET /beneficiaries  4. GET /accounts/\\{AccountId\\}/direct-debits  5. GET /direct-debits  6. GET /standing-orders  7. GET /accounts/\\{AccountId\\}/product  8. GET /products  9. GET /accounts/\\{AccountId\\}/offers  10. GET /offers  11. GET /scheduled-payments  12. GET /statements      ## Error Codes    The error codes and their description can be found  [here](https://openbankinguk.github.io/read-write-api-site3/v3.1.5/profiles/read-write-data-api-profile.html#error-response-structure)      # UK OPB Implementation Specifics     Below you may find more specific information &amp; limitations regarding the implementation followed in the Production API.      ## Token Endpoint Client Authentication    At this point the supported __Client Authentication__ method is \"__Client Secret Basic__\" - usage of \"Client ID\" &amp; \"Client Secret\".      ## Consent Authorization    For a PSU to Authorize a Consent, they need to be redirected to the appropriate Consent UI.    For this redirection to take place the TPP needs to follow the Authorization Endpoint by amending the generated \"Consent ID\", like this: https://my.nbg.gr/identity/connect/authorize?consent_id={{consent_id}}&amp;client_id={{client_id}}&amp;scope={{scope}}&amp;redirect_uri={{redirect_uri}}&amp;response_type=code    Once the PSU is redirected to the Consent Authorization Screen, they need to enter their IBank (Production) or Developer Portal (Sandbox) Credentials and either Authorize or Reject the Consent.    At this point the Consent is binded with the PSU.      ## Debtor Account  Currently, only the \"UK.OBIE.IBAN\" scheme is supported.        # Feedback and Questions    We would love to hear your feedback and answer your questions. Send us at  [developer@nbg.gr](developer@nbg.gr)      Check out our [Sandbox Postman  Collection](https://github.com/NBG-Developer-Portal/Account-Information-UK-Open-Banking)!      ________________________________________    Created by [**NBG**](https://www.nbg.gr/).   # Entities    Below, the main entities are documented.  &lt;a name=OBExternalPermissions1Code&gt;&lt;/a&gt;  ## OBExternalPermissions1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;ReadAccountsBasic&lt;/li&gt;&lt;li&gt;ReadAccountsDetail&lt;/li&gt;&lt;li&gt;ReadBalances&lt;/li&gt;&lt;li&gt;ReadBeneficiariesBasic&lt;/li&gt;&lt;li&gt;ReadBeneficiariesDetail&lt;/li&gt;&lt;li&gt;ReadDirectDebits&lt;/li&gt;&lt;li&gt;ReadOffers&lt;/li&gt;&lt;li&gt;ReadPAN&lt;/li&gt;&lt;li&gt;ReadParty&lt;/li&gt;&lt;li&gt;ReadPartyPSU&lt;/li&gt;&lt;li&gt;ReadProducts&lt;/li&gt;&lt;li&gt;ReadScheduledPaymentsBasic&lt;/li&gt;&lt;li&gt;ReadScheduledPaymentsDetail&lt;/li&gt;&lt;li&gt;ReadStandingOrdersBasic&lt;/li&gt;&lt;li&gt;ReadStandingOrdersDetail&lt;/li&gt;&lt;li&gt;ReadStatementsBasic&lt;/li&gt;&lt;li&gt;ReadStatementsDetail&lt;/li&gt;&lt;li&gt;ReadTransactionsBasic&lt;/li&gt;&lt;li&gt;ReadTransactionsCredits&lt;/li&gt;&lt;li&gt;ReadTransactionsDebits&lt;/li&gt;&lt;li&gt;ReadTransactionsDetail&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBReadData1&gt;&lt;/a&gt;  ## OBReadData1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Permissions| Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP.| array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]| | ExpirationDateTime| Specified date and time the permissions will expire. If this is not populated, the permissions will be open ended. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionFromDateTime| Specified start date and time for the transaction query period. If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionToDateTime| Specified end date and time for the transaction query period. If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=OBRisk2&gt;&lt;/a&gt;  ## OBRisk2  The Risk section is sent by the initiating party to the ASPSP. It is used to specify additional details for risk scoring for Account Info.   ### Attributes   | Name| Description| Values| | -----| -----| -----|   &lt;a name=OBReadConsent1&gt;&lt;/a&gt;  ## OBReadConsent1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadData1](#OBReadData1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Permissions [array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]]&lt;/li&gt; &lt;li&gt;ExpirationDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionFromDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionToDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Risk | Entity | &lt;details&gt;&lt;summary&gt;[OBRisk2](#OBRisk2)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |    &lt;a name=ErrorCode&gt;&lt;/a&gt;  ## ErrorCode  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| This is Data Type gives a low level textual error code to help categorise an error response. The applicable HTTP response code is also given.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;UK.OBIE.Field.Expected&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.Invalid&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.InvalidDate&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.Missing&lt;/li&gt;&lt;li&gt;UK.OBIE.Field.Unexpected&lt;/li&gt;&lt;li&gt;UK.OBIE.Header.Invalid&lt;/li&gt;&lt;li&gt;UK.OBIE.Header.Missing&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.ConsentMismatch&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.InvalidConsentStatus&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.InvalidFormat&lt;/li&gt;&lt;li&gt;UK.OBIE.Resource.NotFound&lt;/li&gt;&lt;li&gt;UK.OBIE.Rules.AfterCutOffDateTime&lt;/li&gt;&lt;li&gt;UK.OBIE.Rules.DuplicateReference&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Invalid&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.InvalidClaim&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.MissingClaim&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Malformed&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Missing&lt;/li&gt;&lt;li&gt;UK.OBIE.Signature.Unexpected&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.AccountIdentifier&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.AccountSecondaryIdentifier&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.Currency&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.EventType&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.Frequency&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.LocalInstrument&lt;/li&gt;&lt;li&gt;UK.OBIE.Unsupported.Scheme&lt;/li&gt;&lt;li&gt;UK.OBIE.Reauthenticate&lt;/li&gt;&lt;li&gt;UK.OBIE.Rules.ResourceAlreadyExists&lt;/li&gt;&lt;li&gt;UK.OBIE.UnexpectedError&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBError1&gt;&lt;/a&gt;  ## OBError1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | ErrorCode | Entity | &lt;details&gt;&lt;summary&gt;[ErrorCode](#ErrorCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Message| A description of the error that occurred. e.g., 'A mandatory field isn't supplied' or 'RequestedExecutionDateTime must be in future'OBIE doesn't standardise this field| string| | Path| Recommended but optional reference to the JSON Path of the field with error, e.g., Data.Initiation.InstructedAmount.Currency| string|   &lt;a name=OBErrorResponse1&gt;&lt;/a&gt;  ## OBErrorResponse1  An array of detail error codes, and messages, and URLs to documentation to help remediation.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | Code| High level textual error code, to help categorize the errors.| string| | Id| A unique reference for the error instance, for audit purposes, in case of unknown/unclassified errors.| string| | Message| Brief Error message, e.g., 'There is something wrong with the request parameters provided'| string| | Errors| Gets or Sets Errors| array[[OBError1](#OBError1)]|   &lt;a name=OBExternalRequestStatus1Code&gt;&lt;/a&gt;  ## OBExternalRequestStatus1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| Specifies the status of consent resource in code form.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Authorised&lt;/li&gt;&lt;li&gt;AwaitingAuthorisation&lt;/li&gt;&lt;li&gt;Rejected&lt;/li&gt;&lt;li&gt;Revoked&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBReadDataConsentResponse1&gt;&lt;/a&gt;  ## OBReadDataConsentResponse1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | ConsentId| Unique identification as assigned to identify the account access consent resource.| string| | CreationDateTime| Date and time at which the resource was created. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Status | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalRequestStatus1Code](#OBExternalRequestStatus1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | StatusUpdateDateTime| Date and time at which the resource status was updated. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Permissions| Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP.| array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]| | ExpirationDateTime| Specified date and time the permissions will expire. If this is not populated, the permissions will be open ended. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionFromDateTime| Specified start date and time for the transaction query period. If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionToDateTime| Specified end date and time for the transaction query period. If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=Links&gt;&lt;/a&gt;  ## Links  Links relevant to the payload   ### Attributes   | Name| Description| Values| | -----| -----| -----| | Self| -| string| | First| -| string| | Prev| -| string| | Next| -| string| | Last| -| string|   &lt;a name=Meta&gt;&lt;/a&gt;  ## Meta  Meta Data relevant to the payload   ### Attributes   | Name| Description| Values| | -----| -----| -----| | TotalPages| -| integer| | FirstAvailableDateTime| All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | LastAvailableDateTime| All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=OBReadConsentResponse1&gt;&lt;/a&gt;  ## OBReadConsentResponse1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataConsentResponse1](#OBReadDataConsentResponse1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;ConsentId [string]&lt;/li&gt; &lt;li&gt;CreationDateTime [string]&lt;/li&gt; &lt;li&gt;&lt;details&gt;&lt;summary&gt;Status [[OBExternalRequestStatus1Code](#OBExternalRequestStatus1Code)]&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;li&gt;StatusUpdateDateTime [string]&lt;/li&gt; &lt;li&gt;Permissions [array[[OBExternalPermissions1Code](#OBExternalPermissions1Code)]]&lt;/li&gt; &lt;li&gt;ExpirationDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionFromDateTime [string]&lt;/li&gt; &lt;li&gt;TransactionToDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Risk | Entity | &lt;details&gt;&lt;summary&gt;[OBRisk2](#OBRisk2)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBExternalAccountType1Code&gt;&lt;/a&gt;  ## OBExternalAccountType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Business&lt;/li&gt;&lt;li&gt;Personal&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBExternalAccountSubType1Code&gt;&lt;/a&gt;  ## OBExternalAccountSubType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;ChargeCard&lt;/li&gt;&lt;li&gt;CreditCard&lt;/li&gt;&lt;li&gt;CurrentAccount&lt;/li&gt;&lt;li&gt;EMoney&lt;/li&gt;&lt;li&gt;Loan&lt;/li&gt;&lt;li&gt;Mortgage&lt;/li&gt;&lt;li&gt;PrePaidCard&lt;/li&gt;&lt;li&gt;Savings&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBCashAccount5&gt;&lt;/a&gt;  ## OBCashAccount5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | SchemeName| Name of the identification scheme, in a coded form as published in an external list.| string| | Identification| Identification assigned by an institution to identify an account. This identification is known by the account owner.| string| | Name| The account name is the name or names of the account owner(s) represented at an account level, as displayed by the ASPSP's online channels. Note, the account name is not the product name or the nickname of the account.| string| | SecondaryIdentification| This is secondary identification of the account, as assigned by the account servicing institution. This can be used by building societies to additionally identify accounts with a roll number(in addition to a sort code and account number combination).| string|   &lt;a name=OBBranchAndFinancialInstitutionIdentification5&gt;&lt;/a&gt;  ## OBBranchAndFinancialInstitutionIdentification5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | SchemeName| Name of the identification scheme, in a coded form as published in an external list.| string| | Identification| Unique and unambiguous identification of the servicing institution.| string|   &lt;a name=OBAccount6&gt;&lt;/a&gt;  ## OBAccount6  Unambiguous identification of the account to which credit and debit entries are made.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | Currency| Identification of the currency in which the account is held.  Usage: Currency should only be used in case one and the same account number covers several currencies and the initiating party needs to identify which currency needs to be used for settlement on the account.| string| | AccountType | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalAccountType1Code](#OBExternalAccountType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | AccountSubType | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalAccountSubType1Code](#OBExternalAccountSubType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Description| Specifies the description of the account type.| string| | Nickname| The nickname of the account, assigned by the account owner in order to provide an additional means of identification of the account.| string| | OpeningDate| Date on which the account and related basic services are effectively operational for the account owner.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Account| Provides the details to identify an account.| array[[OBCashAccount5](#OBCashAccount5)]| | Servicer | Entity | &lt;details&gt;&lt;summary&gt;[OBBranchAndFinancialInstitutionIdentification5](#OBBranchAndFinancialInstitutionIdentification5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataAccount5&gt;&lt;/a&gt;  ## OBReadDataAccount5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Account| Unambiguous identification of the account to which credit and debit entries are made.| array[[OBAccount6](#OBAccount6)]|   &lt;a name=OBReadAccount5&gt;&lt;/a&gt;  ## OBReadAccount5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataAccount5](#OBReadDataAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Account [array[[OBAccount6](#OBAccount6)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBCreditDebitCode&gt;&lt;/a&gt;  ## OBCreditDebitCode  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Credit&lt;/li&gt;&lt;li&gt;Debit&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBBalanceType1Code&gt;&lt;/a&gt;  ## OBBalanceType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;ClosingAvailable&lt;/li&gt;&lt;li&gt;ClosingBooked&lt;/li&gt;&lt;li&gt;ClosingCleared&lt;/li&gt;&lt;li&gt;Expected&lt;/li&gt;&lt;li&gt;ForwardAvailable&lt;/li&gt;&lt;li&gt;Information&lt;/li&gt;&lt;li&gt;InterimAvailable&lt;/li&gt;&lt;li&gt;InterimBooked&lt;/li&gt;&lt;li&gt;InterimCleared&lt;/li&gt;&lt;li&gt;OpeningAvailable&lt;/li&gt;&lt;li&gt;OpeningBooked&lt;/li&gt;&lt;li&gt;OpeningCleared&lt;/li&gt;&lt;li&gt;PreviouslyClosedBooked&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBActiveOrHistoricCurrencyAndAmount&gt;&lt;/a&gt;  ## OBActiveOrHistoricCurrencyAndAmount    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Amount| A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217.| string| | Currency| A code allocated to a currency by a Maintenance Agency under an international identification scheme, as described in the latest edition of the international standard ISO 4217 \"Codes for the representation of currencies and funds\".| string|   &lt;a name=OBExternalLimitType1Code&gt;&lt;/a&gt;  ## OBExternalLimitType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Available&lt;/li&gt;&lt;li&gt;Credit&lt;/li&gt;&lt;li&gt;Emergency&lt;/li&gt;&lt;li&gt;Pre-Agreed&lt;/li&gt;&lt;li&gt;Temporary&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBCreditLine1&gt;&lt;/a&gt;  ## OBCreditLine1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Included| Indicates whether or not the credit line is included in the balance of the account. Usage: If not present, credit line is not included in the balance amount of the account.| boolean| | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalLimitType1Code](#OBExternalLimitType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBCashBalance1&gt;&lt;/a&gt;  ## OBCashBalance1  Set of elements used to define the balance details.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | CreditDebitIndicator | Entity | &lt;details&gt;&lt;summary&gt;[OBCreditDebitCode](#OBCreditDebitCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBBalanceType1Code](#OBBalanceType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | DateTime| Indicates the date (and time) of the balance.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00| string| | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | CreditLine| Set of elements used to provide details on the credit line.| array[[OBCreditLine1](#OBCreditLine1)]|   &lt;a name=OBReadDataBalance1&gt;&lt;/a&gt;  ## OBReadDataBalance1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Balance| Set of elements used to define the balance details.| array[[OBCashBalance1](#OBCashBalance1)]|   &lt;a name=OBReadBalance1&gt;&lt;/a&gt;  ## OBReadBalance1    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataBalance1](#OBReadDataBalance1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Balance [array[[OBCashBalance1](#OBCashBalance1)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBBeneficiaryType1Code&gt;&lt;/a&gt;  ## OBBeneficiaryType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| Specifies the Beneficiary Type.| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Trusted&lt;/li&gt;&lt;li&gt;Ordinary&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBBeneficiary5&gt;&lt;/a&gt;  ## OBBeneficiary5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | BeneficiaryType | Entity | &lt;details&gt;&lt;summary&gt;[OBBeneficiaryType1Code](#OBBeneficiaryType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount5](#OBCashAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;li&gt;SecondaryIdentification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataBeneficiary5&gt;&lt;/a&gt;  ## OBReadDataBeneficiary5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Beneficiary| -| array[[OBBeneficiary5](#OBBeneficiary5)]|   &lt;a name=OBReadBeneficiary5&gt;&lt;/a&gt;  ## OBReadBeneficiary5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataBeneficiary5](#OBReadDataBeneficiary5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Beneficiary [array[[OBBeneficiary5](#OBBeneficiary5)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBParty2&gt;&lt;/a&gt;  ## OBParty2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | PartyId| A unique and immutable identifier used to identify the customer resource. This identifier has no meaning to the account owner.| string| | Name| Name by which a party is known and which is usually used to identify that party.| string|   &lt;a name=OBReadDataParty2&gt;&lt;/a&gt;  ## OBReadDataParty2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Party | Entity | &lt;details&gt;&lt;summary&gt;[OBParty2](#OBParty2)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;PartyId [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadParty2&gt;&lt;/a&gt;  ## OBReadParty2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataParty2](#OBReadDataParty2)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;Party [[OBParty2](#OBParty2)]&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;PartyId [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataParty3&gt;&lt;/a&gt;  ## OBReadDataParty3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Party| -| array[[OBParty2](#OBParty2)]|   &lt;a name=OBReadParty3&gt;&lt;/a&gt;  ## OBReadParty3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataParty3](#OBReadDataParty3)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Party [array[[OBParty2](#OBParty2)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=SandboxRequest&gt;&lt;/a&gt;  ## SandboxRequest  Request to create a new sandbox   ### Attributes   | Name| Description| Values| | -----| -----| -----| | sandboxId| Sandbox Id| string|   &lt;a name=ErrorResponse&gt;&lt;/a&gt;  ## ErrorResponse    ### Attributes   | Name| Description| Values| | -----| -----| -----| | errorMessage| -| string|   &lt;a name=SandboxRetryCacheEntry&gt;&lt;/a&gt;  ## SandboxRetryCacheEntry  Keeps the number of calls without x-fapi-customer-ip-address header present   ### Attributes   | Name| Description| Values| | -----| -----| -----| | cacheKey| Cache key| string| | count| Number of retries ( up to 4 )| integer| | expirationTimestamp| Expiration timestamp of the entry| string|   &lt;a name=SandboxBankAccountInfo&gt;&lt;/a&gt;  ## SandboxBankAccountInfo  General account information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | currency| Currency (EUR, USD ...)| string| | iban| Account's IBAN| string| | accountType| Account's type (Business, Personal)| string| | accountSubType| Account's sub-type (ChargeCard, CreditCard, CurrentAccount ...)| string| | description| Account's description| string| | alias| Account's alias| string| | openingDate| Account's opening date| string| | availableBalance| Account's available balance| number| | ledgerBalance| Account's ledger balance| number| | overdraftLimit| Account's overdraft limit| number|   &lt;a name=SandboxParty&gt;&lt;/a&gt;  ## SandboxParty  Connected party information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | id| Party id| string| | name| Name| string|   &lt;a name=SandboxBeneficiary&gt;&lt;/a&gt;  ## SandboxBeneficiary  Beneficiary information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | name| Beneficiary name| string|   &lt;a name=SandboxStandingOrder&gt;&lt;/a&gt;  ## SandboxStandingOrder  Standing order information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | description| Standing order short description| string| | frequency| Standing order frequency| string| | firstPaymentDate| Standing order first collection date| string| | nextPaymentDate| Standing order next collection date| string| | finalPaymentDate| Standing order final collection date| string| | lastPaymentDate| Standing order last executed payment date| string| | status| Standing order status (Active, Inactive)| string| | amount| Standing order amount| number|   &lt;a name=SandboxScheduledPayment&gt;&lt;/a&gt;  ## SandboxScheduledPayment  Scheduled payment information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | description| Scheduled payment's short description| string| | executionDate| Scheduled payment's execution date| string| | amount| Amount| number| | senderReference| Debtor / Sender reference| string|   &lt;a name=SandboxStatement&gt;&lt;/a&gt;  ## SandboxStatement  Statement information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | number| Statement number| string| | year| Statement year| integer| | month| Statement month| integer|   &lt;a name=SandboxTransaction&gt;&lt;/a&gt;  ## SandboxTransaction  Transaction information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | reference| Transaction reference| string| | amount| Amount| number| | currency| Currency (EUR, USD ...)| string| | creditDebit| Credit / Debit indicator| string| | valueDateTime| Valeur| string| | bookingDateTime| Booking date time| string| | description| Description| string| | accountingBalance| Balance| number| | relatedAccount| Related account| string| | relatedName| Related account| string| | transactionCode| Transaction code| string|   &lt;a name=SandboxBankAccount&gt;&lt;/a&gt;  ## SandboxBankAccount  Sandbox bank account   ### Attributes   | Name| Description| Values| | -----| -----| -----| | info | Entity | &lt;details&gt;&lt;summary&gt;[SandboxBankAccountInfo](#SandboxBankAccountInfo)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;currency [string]&lt;/li&gt; &lt;li&gt;iban [string]&lt;/li&gt; &lt;li&gt;accountType [string]&lt;/li&gt; &lt;li&gt;accountSubType [string]&lt;/li&gt; &lt;li&gt;description [string]&lt;/li&gt; &lt;li&gt;alias [string]&lt;/li&gt; &lt;li&gt;openingDate [string]&lt;/li&gt; &lt;li&gt;availableBalance [number]&lt;/li&gt; &lt;li&gt;ledgerBalance [number]&lt;/li&gt; &lt;li&gt;overdraftLimit [number]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | party | Entity | &lt;details&gt;&lt;summary&gt;[SandboxParty](#SandboxParty)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;id [string]&lt;/li&gt; &lt;li&gt;name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | beneficiaries| List of account's beneficiaries| array[[SandboxBeneficiary](#SandboxBeneficiary)]| | standingOrders| List of account's standing orders| array[[SandboxStandingOrder](#SandboxStandingOrder)]| | scheduledPayments| List of account's scheduled payments| array[[SandboxScheduledPayment](#SandboxScheduledPayment)]| | statements| List of account's statements| array[[SandboxStatement](#SandboxStatement)]| | transactions| List of account's transactions| array[[SandboxTransaction](#SandboxTransaction)]|   &lt;a name=SandboxCardInfo&gt;&lt;/a&gt;  ## SandboxCardInfo  Sandbox card information   ### Attributes   | Name| Description| Values| | -----| -----| -----| | number| Card number| string| | description| Description| string| | holderName| Holder name| string| | expiration| Expiration date (05/2022)| string| | type| Type| string| | subType| Sub type| string| | availableBalance| Available balance| number| | ledgerBalance| Ledger balance| number| | creditLimit| Credit limit ( applicable to credit cards )| number|   &lt;a name=SandboxCard&gt;&lt;/a&gt;  ## SandboxCard  Sandbox card   ### Attributes   | Name| Description| Values| | -----| -----| -----| | info | Entity | &lt;details&gt;&lt;summary&gt;[SandboxCardInfo](#SandboxCardInfo)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;number [string]&lt;/li&gt; &lt;li&gt;description [string]&lt;/li&gt; &lt;li&gt;holderName [string]&lt;/li&gt; &lt;li&gt;expiration [string]&lt;/li&gt; &lt;li&gt;type [string]&lt;/li&gt; &lt;li&gt;subType [string]&lt;/li&gt; &lt;li&gt;availableBalance [number]&lt;/li&gt; &lt;li&gt;ledgerBalance [number]&lt;/li&gt; &lt;li&gt;creditLimit [number]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | party | Entity | &lt;details&gt;&lt;summary&gt;[SandboxParty](#SandboxParty)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;id [string]&lt;/li&gt; &lt;li&gt;name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | statements| Card statements| array[[SandboxStatement](#SandboxStatement)]| | transactions| Card transactions| array[[SandboxTransaction](#SandboxTransaction)]|   &lt;a name=SandboxUser&gt;&lt;/a&gt;  ## SandboxUser  User data   ### Attributes   | Name| Description| Values| | -----| -----| -----| | userId| Connected user id| string| | retryCacheEntries| Retry cache entries| array[[SandboxRetryCacheEntry](#SandboxRetryCacheEntry)]| | accounts| List of accounts| array[[SandboxBankAccount](#SandboxBankAccount)]| | cards| List of cards| array[[SandboxCard](#SandboxCard)]|   &lt;a name=Sandbox&gt;&lt;/a&gt;  ## Sandbox  Sandbox model   ### Attributes   | Name| Description| Values| | -----| -----| -----| | sandboxId| Sandbox id| string| | users| List of users| array[[SandboxUser](#SandboxUser)]|   &lt;a name=OBExternalScheduleType1Code&gt;&lt;/a&gt;  ## OBExternalScheduleType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Arrival&lt;/li&gt;&lt;li&gt;Execution&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBScheduledPayment3&gt;&lt;/a&gt;  ## OBScheduledPayment3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | ScheduledPaymentId| A unique and immutable identifier used to identify the scheduled payment resource. This identifier has no meaning to the account owner.| string| | ScheduledPaymentDateTime| The date on which the scheduled payment will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | ScheduledType | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalScheduleType1Code](#OBExternalScheduleType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Reference| Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. Usage: If available, the initiating party should provide this reference in the structured remittance information, to enable reconciliation by the creditor upon receipt of the amount of money. If the business context requires the use of a creditor reference or a payment remit identification, and only one identifier can be passed through the end-to-end chain, the creditor's reference or payment remittance identification should be quoted in the end-to-end transaction identification.| string| | DebtorReference| A reference value provided by the PSU to the PISP while setting up the scheduled payment.| string| | InstructedAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount5](#OBCashAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;li&gt;SecondaryIdentification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataScheduledPayment3&gt;&lt;/a&gt;  ## OBReadDataScheduledPayment3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | ScheduledPayment| -| array[[OBScheduledPayment3](#OBScheduledPayment3)]|   &lt;a name=OBReadScheduledPayment3&gt;&lt;/a&gt;  ## OBReadScheduledPayment3    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataScheduledPayment3](#OBReadDataScheduledPayment3)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;ScheduledPayment [array[[OBScheduledPayment3](#OBScheduledPayment3)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBExternalStandingOrderStatus1Code&gt;&lt;/a&gt;  ## OBExternalStandingOrderStatus1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Active&lt;/li&gt;&lt;li&gt;Inactive&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBStandingOrder5&gt;&lt;/a&gt;  ## OBStandingOrder5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | StandingOrderId| A unique and immutable identifier used to identify the standing order resource. This identifier has no meaning to the account owner.| string| | Frequency| Individual Definitions: IntrvlMnthDay - An interval specified in months(between 01, 02, 03, 04, 06, 12, 24), specifying the day within the month(01 to 31) Full Regular Expression: ^(IntrvlMnthDay:(0[1,2,3,4,6]|12|24):(0[1-9]|[12] [0-9]|3[01]))$| string| | Reference| Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction. Usage: If available, the initiating party should provide this reference in the structured remittance information, to enable reconciliation by the creditor upon receipt of the amount of money. If the business context requires the use of a creditor reference or a payment remit identification, and only one identifier can be passed through the end-to-end chain, the creditor's reference or payment remittance identification should be quoted in the end-to-end transaction identification.| string| | FirstPaymentDateTime| The date on which the first payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | NextPaymentDateTime| The date on which the next payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | LastPaymentDateTime| The date on which the last (most recent) payment for a Standing Order schedule was made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | FinalPaymentDateTime| The date on which the final payment for a Standing Order schedule will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | StandingOrderStatusCode | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalStandingOrderStatus1Code](#OBExternalStandingOrderStatus1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | FirstPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | NextPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | LastPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | FinalPaymentAmount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount5](#OBCashAccount5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;li&gt;SecondaryIdentification [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataStandingOrder5&gt;&lt;/a&gt;  ## OBReadDataStandingOrder5    ### Attributes   | Name| Description| Values| | -----| -----| -----| | StandingOrder| -| array[[OBStandingOrder5](#OBStandingOrder5)]|   &lt;a name=OBReadStandingOrder6&gt;&lt;/a&gt;  ## OBReadStandingOrder6    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataStandingOrder5](#OBReadDataStandingOrder5)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;StandingOrder [array[[OBStandingOrder5](#OBStandingOrder5)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBExternalStatementType1Code&gt;&lt;/a&gt;  ## OBExternalStatementType1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;AccountClosure&lt;/li&gt;&lt;li&gt;AccountOpening&lt;/li&gt;&lt;li&gt;Annual&lt;/li&gt;&lt;li&gt;Interim&lt;/li&gt;&lt;li&gt;RegularPeriodic&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=OBStatement2&gt;&lt;/a&gt;  ## OBStatement2  Provides further details on a statement resource.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | StatementId| Unique identifier for the statement resource within an servicing institution. This identifier is both unique and immutable.| string| | StatementReference| Unique reference for the statement. This reference may be optionally populated if available.| string| | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBExternalStatementType1Code](#OBExternalStatementType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | StartDateTime| Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | EndDateTime| Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | CreationDateTime| Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string|   &lt;a name=OBReadDataStatement2&gt;&lt;/a&gt;  ## OBReadDataStatement2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Statement| Provides further details on a statement resource.| array[[OBStatement2](#OBStatement2)]|   &lt;a name=OBReadStatement2&gt;&lt;/a&gt;  ## OBReadStatement2    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataStatement2](#OBReadDataStatement2)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Statement [array[[OBStatement2](#OBStatement2)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBEntryStatus1Code&gt;&lt;/a&gt;  ## OBEntryStatus1Code  ### Attributes   | Type| Description| Example| Values| | -----| -----| -----| -----| | enum| -| &lt;ul style=\"padding-left: 0\"&gt;&lt;li&gt;Booked&lt;/li&gt;&lt;li&gt;Pending&lt;/li&gt;&lt;/ul&gt;|   &lt;a name=ProprietaryBankTransactionCodeStructure1&gt;&lt;/a&gt;  ## ProprietaryBankTransactionCodeStructure1  Set of elements to fully identify a proprietary bank transaction code.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | Code| Proprietary bank transaction code to identify the underlying transaction.| string| | Issuer| Identification of the issuer of the proprietary bank transaction code.| string|   &lt;a name=OBTransactionCashBalance&gt;&lt;/a&gt;  ## OBTransactionCashBalance  Set of elements used to define the balance as a numerical representation of the net increases and decreases in an account after a transaction entry is applied to the account.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | CreditDebitIndicator | Entity | &lt;details&gt;&lt;summary&gt;[OBCreditDebitCode](#OBCreditDebitCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Type | Entity | &lt;details&gt;&lt;summary&gt;[OBBalanceType1Code](#OBBalanceType1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBCashAccount6&gt;&lt;/a&gt;  ## OBCashAccount6  Unambiguous identification of the account of the creditor, in the case of a debit transaction.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | SchemeName| Name of the identification scheme, in a coded form as published in an external list.| string| | Identification| Identification assigned by an institution to identify an account. This identification is known by the account owner.| string| | Name| The account name is the name or names of the account owner(s) represented at an account level, as displayed by the ASPSP's online channels. Note, the account name is not the product name or the nickname of the account.| string|   &lt;a name=OBTransaction6&gt;&lt;/a&gt;  ## OBTransaction6  Provides further details on an entry in the report.   ### Attributes   | Name| Description| Values| | -----| -----| -----| | AccountId| A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner.| string| | TransactionReference| Unique reference for the transaction. This reference is optionally populated, and may as an example be the FPID in the Faster Payments context.| string| | CreditDebitIndicator | Entity | &lt;details&gt;&lt;summary&gt;[OBCreditDebitCode](#OBCreditDebitCode)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | Status | Entity | &lt;details&gt;&lt;summary&gt;[OBEntryStatus1Code](#OBEntryStatus1Code)&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt; |  | BookingDateTime| Date and time when a transaction entry is posted to an account on the account servicer's books. Usage: Booking date is the expected booking date, unless the status is booked, in which case it is the actual booking date.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | ValueDateTime| Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit transaction entry. Usage: If transaction entry status is pending and value date is present, then the value date refers to an expected/requested value date. For transaction entries subject to availability/float and for which availability information is provided, the value date must not be used.In this case the availability component identifies the number of availability days.All dates in the JSON payloads are represented in ISO 8601 date-time format. All date-time fields in responses must include the timezone.An example is below: 2017-04-05T10:43:07+00:00| string| | TransactionInformation| Further details of the transaction. This is the transaction narrative, which is unstructured text.| string| | Amount | Entity | &lt;details&gt;&lt;summary&gt;[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | ProprietaryBankTransactionCode | Entity | &lt;details&gt;&lt;summary&gt;[ProprietaryBankTransactionCodeStructure1](#ProprietaryBankTransactionCodeStructure1)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Code [string]&lt;/li&gt; &lt;li&gt;Issuer [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Balance | Entity | &lt;details&gt;&lt;summary&gt;[OBTransactionCashBalance](#OBTransactionCashBalance)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;CreditDebitIndicator [[OBCreditDebitCode](#OBCreditDebitCode)]&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;Type [[OBBalanceType1Code](#OBBalanceType1Code)]&lt;/summary&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;li&gt;&lt;details&gt;&lt;summary&gt;Amount [[OBActiveOrHistoricCurrencyAndAmount](#OBActiveOrHistoricCurrencyAndAmount)]&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Amount [string]&lt;/li&gt; &lt;li&gt;Currency [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/details&gt; |  | CreditorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount6](#OBCashAccount6)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | DebtorAccount | Entity | &lt;details&gt;&lt;summary&gt;[OBCashAccount6](#OBCashAccount6)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;SchemeName [string]&lt;/li&gt; &lt;li&gt;Identification [string]&lt;/li&gt; &lt;li&gt;Name [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |    &lt;a name=OBReadDataTransaction6&gt;&lt;/a&gt;  ## OBReadDataTransaction6    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Transaction| Provides further details on an entry in the report.| array[[OBTransaction6](#OBTransaction6)]|   &lt;a name=OBReadTransaction6&gt;&lt;/a&gt;  ## OBReadTransaction6    ### Attributes   | Name| Description| Values| | -----| -----| -----| | Data | Entity | &lt;details&gt;&lt;summary&gt;[OBReadDataTransaction6](#OBReadDataTransaction6)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Transaction [array[[OBTransaction6](#OBTransaction6)]]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Links | Entity | &lt;details&gt;&lt;summary&gt;[Links](#Links)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;Self [string]&lt;/li&gt; &lt;li&gt;First [string]&lt;/li&gt; &lt;li&gt;Prev [string]&lt;/li&gt; &lt;li&gt;Next [string]&lt;/li&gt; &lt;li&gt;Last [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |  | Meta | Entity | &lt;details&gt;&lt;summary&gt;[Meta](#Meta)&lt;/summary&gt;&lt;ul&gt;&lt;li&gt;TotalPages [integer]&lt;/li&gt; &lt;li&gt;FirstAvailableDateTime [string]&lt;/li&gt; &lt;li&gt;LastAvailableDateTime [string]&lt;/li&gt; &lt;/ul&gt;&lt;/details&gt; |   # Authentication  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;
 *
 * The version of the OpenAPI document: v3.1.5
 * Contact: developer@nbg.gr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import superagent from "superagent";
import querystring from "querystring";

/**
* @module ApiClient
* @version v3.1.5
*/

/**
* Manages low level client-server communications, parameter marshalling, etc. There should not be any need for an
* application to use this class directly - the *Api and model classes provide the public API for the service. The
* contents of this file should be regarded as internal but are documented for completeness.
* @alias module:ApiClient
* @class
*/
class ApiClient {
    /**
     * The base URL against which to resolve every API call's (relative) path.
     * Overrides the default value set in spec file if present
     * @param {String} basePath
     */
    constructor(basePath = 'https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5') {
        /**
         * The base URL against which to resolve every API call's (relative) path.
         * @type {String}
         * @default https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5
         */
        this.basePath = basePath.replace(/\/+$/, '');

        /**
         * The authentication methods to be included for all API calls.
         * @type {Array.<String>}
         */
        this.authentications = {
            'Authorization-Code-Token': {type: 'oauth2'},
            'Client-Credentials-Token': {type: 'oauth2'},
            'Client-Id': {type: 'apiKey', 'in': 'header', name: 'Client-Id'}
        }

        /**
         * The default HTTP headers to be included for all API calls.
         * @type {Array.<String>}
         * @default {}
         */
        this.defaultHeaders = {
            'User-Agent': 'OpenAPI-Generator/v3.1.5/Javascript'
        };

        /**
         * The default HTTP timeout for all API calls.
         * @type {Number}
         * @default 60000
         */
        this.timeout = 60000;

        /**
         * If set to false an additional timestamp parameter is added to all API GET calls to
         * prevent browser caching
         * @type {Boolean}
         * @default true
         */
        this.cache = true;

        /**
         * If set to true, the client will save the cookies from each server
         * response, and return them in the next request.
         * @default false
         */
        this.enableCookies = false;

        /*
         * Used to save and return cookies in a node.js (non-browser) setting,
         * if this.enableCookies is set to true.
         */
        if (typeof window === 'undefined') {
          this.agent = new superagent.agent();
        }

        /*
         * Allow user to override superagent agent
         */
         this.requestAgent = null;

        /*
         * Allow user to add superagent plugins
         */
        this.plugins = null;

    }

    /**
    * Returns a string representation for an actual parameter.
    * @param param The actual parameter.
    * @returns {String} The string representation of <code>param</code>.
    */
    paramToString(param) {
        if (param == undefined || param == null) {
            return '';
        }
        if (param instanceof Date) {
            return param.toJSON();
        }
        if (ApiClient.canBeJsonified(param)) {
            return JSON.stringify(param);
        }

        return param.toString();
    }

    /**
    * Returns a boolean indicating if the parameter could be JSON.stringified
    * @param param The actual parameter
    * @returns {Boolean} Flag indicating if <code>param</code> can be JSON.stringified
    */
    static canBeJsonified(str) {
        if (typeof str !== 'string' && typeof str !== 'object') return false;
        try {
            const type = str.toString();
            return type === '[object Object]'
                || type === '[object Array]';
        } catch (err) {
            return false;
        }
    };

   /**
    * Builds full URL by appending the given path to the base URL and replacing path parameter place-holders with parameter values.
    * NOTE: query parameters are not handled here.
    * @param {String} path The path to append to the base URL.
    * @param {Object} pathParams The parameter values to append.
    * @param {String} apiBasePath Base path defined in the path, operation level to override the default one
    * @returns {String} The encoded path with parameter values substituted.
    */
    buildUrl(path, pathParams, apiBasePath) {
        if (!path.match(/^\//)) {
            path = '/' + path;
        }

        var url = this.basePath + path;

        // use API (operation, path) base path if defined
        if (apiBasePath !== null && apiBasePath !== undefined) {
            url = apiBasePath + path;
        }

        url = url.replace(/\{([\w-\.#]+)\}/g, (fullMatch, key) => {
            var value;
            if (pathParams.hasOwnProperty(key)) {
                value = this.paramToString(pathParams[key]);
            } else {
                value = fullMatch;
            }

            return encodeURIComponent(value);
        });

        return url;
    }

    /**
    * Checks whether the given content type represents JSON.<br>
    * JSON content type examples:<br>
    * <ul>
    * <li>application/json</li>
    * <li>application/json; charset=UTF8</li>
    * <li>APPLICATION/JSON</li>
    * </ul>
    * @param {String} contentType The MIME content type to check.
    * @returns {Boolean} <code>true</code> if <code>contentType</code> represents JSON, otherwise <code>false</code>.
    */
    isJsonMime(contentType) {
        return Boolean(contentType != null && contentType.match(/^application\/json(;.*)?$/i));
    }

    /**
    * Chooses a content type from the given array, with JSON preferred; i.e. return JSON if included, otherwise return the first.
    * @param {Array.<String>} contentTypes
    * @returns {String} The chosen content type, preferring JSON.
    */
    jsonPreferredMime(contentTypes) {
        for (var i = 0; i < contentTypes.length; i++) {
            if (this.isJsonMime(contentTypes[i])) {
                return contentTypes[i];
            }
        }

        return contentTypes[0];
    }

    /**
    * Checks whether the given parameter value represents file-like content.
    * @param param The parameter to check.
    * @returns {Boolean} <code>true</code> if <code>param</code> represents a file.
    */
    isFileParam(param) {
        // fs.ReadStream in Node.js and Electron (but not in runtime like browserify)
        if (typeof require === 'function') {
            let fs;
            try {
                fs = require('fs');
            } catch (err) {}
            if (fs && fs.ReadStream && param instanceof fs.ReadStream) {
                return true;
            }
        }

        // Buffer in Node.js
        if (typeof Buffer === 'function' && param instanceof Buffer) {
            return true;
        }

        // Blob in browser
        if (typeof Blob === 'function' && param instanceof Blob) {
            return true;
        }

        // File in browser (it seems File object is also instance of Blob, but keep this for safe)
        if (typeof File === 'function' && param instanceof File) {
            return true;
        }

        return false;
    }

    /**
    * Normalizes parameter values:
    * <ul>
    * <li>remove nils</li>
    * <li>keep files and arrays</li>
    * <li>format to string with `paramToString` for other cases</li>
    * </ul>
    * @param {Object.<String, Object>} params The parameters as object properties.
    * @returns {Object.<String, Object>} normalized parameters.
    */
    normalizeParams(params) {
        var newParams = {};
        for (var key in params) {
            if (params.hasOwnProperty(key) && params[key] != undefined && params[key] != null) {
                var value = params[key];
                if (this.isFileParam(value) || Array.isArray(value)) {
                    newParams[key] = value;
                } else {
                    newParams[key] = this.paramToString(value);
                }
            }
        }

        return newParams;
    }

    /**
    * Builds a string representation of an array-type actual parameter, according to the given collection format.
    * @param {Array} param An array parameter.
    * @param {module:ApiClient.CollectionFormatEnum} collectionFormat The array element separator strategy.
    * @returns {String|Array} A string representation of the supplied collection, using the specified delimiter. Returns
    * <code>param</code> as is if <code>collectionFormat</code> is <code>multi</code>.
    */
    buildCollectionParam(param, collectionFormat) {
        if (param == null) {
            return null;
        }
        switch (collectionFormat) {
            case 'csv':
                return param.map(this.paramToString, this).join(',');
            case 'ssv':
                return param.map(this.paramToString, this).join(' ');
            case 'tsv':
                return param.map(this.paramToString, this).join('\t');
            case 'pipes':
                return param.map(this.paramToString, this).join('|');
            case 'multi':
                //return the array directly as SuperAgent will handle it as expected
                return param.map(this.paramToString, this);
            case 'passthrough':
                return param;
            default:
                throw new Error('Unknown collection format: ' + collectionFormat);
        }
    }

    /**
    * Applies authentication headers to the request.
    * @param {Object} request The request object created by a <code>superagent()</code> call.
    * @param {Array.<String>} authNames An array of authentication method names.
    */
    applyAuthToRequest(request, authNames) {
        authNames.forEach((authName) => {
            var auth = this.authentications[authName];
            switch (auth.type) {
                case 'basic':
                    if (auth.username || auth.password) {
                        request.auth(auth.username || '', auth.password || '');
                    }

                    break;
                case 'bearer':
                    if (auth.accessToken) {
                        var localVarBearerToken = typeof auth.accessToken === 'function'
                          ? auth.accessToken()
                          : auth.accessToken
                        request.set({'Authorization': 'Bearer ' + localVarBearerToken});
                    }

                    break;
                case 'apiKey':
                    if (auth.apiKey) {
                        var data = {};
                        if (auth.apiKeyPrefix) {
                            data[auth.name] = auth.apiKeyPrefix + ' ' + auth.apiKey;
                        } else {
                            data[auth.name] = auth.apiKey;
                        }

                        if (auth['in'] === 'header') {
                            request.set(data);
                        } else {
                            request.query(data);
                        }
                    }

                    break;
                case 'oauth2':
                    if (auth.accessToken) {
                        request.set({'Authorization': 'Bearer ' + auth.accessToken});
                    }

                    break;
                default:
                    throw new Error('Unknown authentication type: ' + auth.type);
            }
        });
    }

   /**
    * Deserializes an HTTP response body into a value of the specified type.
    * @param {Object} response A SuperAgent response object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} returnType The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns A value of the specified type.
    */
    deserialize(response, returnType) {
        if (response == null || returnType == null || response.status == 204) {
            return null;
        }

        // Rely on SuperAgent for parsing response body.
        // See http://visionmedia.github.io/superagent/#parsing-response-bodies
        var data = response.body;
        if (data == null || (typeof data === 'object' && typeof data.length === 'undefined' && !Object.keys(data).length)) {
            // SuperAgent does not always produce a body; use the unparsed response as a fallback
            data = response.text;
        }

        return ApiClient.convertToType(data, returnType);
    }

   /**
    * Callback function to receive the result of the operation.
    * @callback module:ApiClient~callApiCallback
    * @param {String} error Error message, if any.
    * @param data The data returned by the service call.
    * @param {String} response The complete HTTP response.
    */

   /**
    * Invokes the REST service using the supplied settings and parameters.
    * @param {String} path The base URL to invoke.
    * @param {String} httpMethod The HTTP method to use.
    * @param {Object.<String, String>} pathParams A map of path parameters and their values.
    * @param {Object.<String, Object>} queryParams A map of query parameters and their values.
    * @param {Object.<String, Object>} headerParams A map of header parameters and their values.
    * @param {Object.<String, Object>} formParams A map of form parameters and their values.
    * @param {Object} bodyParam The value to pass as the request body.
    * @param {Array.<String>} authNames An array of authentication type names.
    * @param {Array.<String>} contentTypes An array of request MIME types.
    * @param {Array.<String>} accepts An array of acceptable response MIME types.
    * @param {(String|Array|ObjectFunction)} returnType The required type to return; can be a string for simple types or the
    * constructor for a complex type.
    * @param {String} apiBasePath base path defined in the operation/path level to override the default one
    * @param {module:ApiClient~callApiCallback} callback The callback function.
    * @returns {Object} The SuperAgent request object.
    */
    callApi(path, httpMethod, pathParams,
        queryParams, headerParams, formParams, bodyParam, authNames, contentTypes, accepts,
        returnType, apiBasePath, callback) {

        var url = this.buildUrl(path, pathParams, apiBasePath);
        var request = superagent(httpMethod, url);

        if (this.plugins !== null) {
            for (var index in this.plugins) {
                if (this.plugins.hasOwnProperty(index)) {
                    request.use(this.plugins[index])
                }
            }
        }

        // apply authentications
        this.applyAuthToRequest(request, authNames);

        // set query parameters
        if (httpMethod.toUpperCase() === 'GET' && this.cache === false) {
            queryParams['_'] = new Date().getTime();
        }

        request.query(this.normalizeParams(queryParams));

        // set header parameters
        request.set(this.defaultHeaders).set(this.normalizeParams(headerParams));

        // set requestAgent if it is set by user
        if (this.requestAgent) {
          request.agent(this.requestAgent);
        }

        // set request timeout
        request.timeout(this.timeout);

        var contentType = this.jsonPreferredMime(contentTypes);
        if (contentType) {
            // Issue with superagent and multipart/form-data (https://github.com/visionmedia/superagent/issues/746)
            if(contentType != 'multipart/form-data') {
                request.type(contentType);
            }
        }

        if (contentType === 'application/x-www-form-urlencoded') {
            request.send(querystring.stringify(this.normalizeParams(formParams)));
        } else if (contentType == 'multipart/form-data') {
            var _formParams = this.normalizeParams(formParams);
            for (var key in _formParams) {
                if (_formParams.hasOwnProperty(key)) {
                    let _formParamsValue = _formParams[key];
                    if (this.isFileParam(_formParamsValue)) {
                        // file field
                        request.attach(key, _formParamsValue);
                    } else if (Array.isArray(_formParamsValue) && _formParamsValue.length
                        && this.isFileParam(_formParamsValue[0])) {
                        // multiple files
                        _formParamsValue.forEach(file => request.attach(key, file));
                    } else {
                        request.field(key, _formParamsValue);
                    }
                }
            }
        } else if (bodyParam !== null && bodyParam !== undefined) {
            if (!request.header['Content-Type']) {
                request.type('application/json');
            }
            request.send(bodyParam);
        }

        var accept = this.jsonPreferredMime(accepts);
        if (accept) {
            request.accept(accept);
        }

        if (returnType === 'Blob') {
          request.responseType('blob');
        } else if (returnType === 'String') {
          request.responseType('text');
        }

        // Attach previously saved cookies, if enabled
        if (this.enableCookies){
            if (typeof window === 'undefined') {
                this.agent._attachCookies(request);
            }
            else {
                request.withCredentials();
            }
        }

        request.end((error, response) => {
            if (callback) {
                var data = null;
                if (!error) {
                    try {
                        data = this.deserialize(response, returnType);
                        if (this.enableCookies && typeof window === 'undefined'){
                            this.agent._saveCookies(response);
                        }
                    } catch (err) {
                        error = err;
                    }
                }

                callback(error, data, response);
            }
        });

        return request;
    }

    /**
    * Parses an ISO-8601 string representation or epoch representation of a date value.
    * @param {String} str The date value as a string.
    * @returns {Date} The parsed date object.
    */
    static parseDate(str) {
        if (isNaN(str)) {
            return new Date(str.replace(/(\d)(T)(\d)/i, '$1 $3'));
        }
        return new Date(+str);
    }

    /**
    * Converts a value to the specified type.
    * @param {(String|Object)} data The data to convert, as a string or object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} type The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns An instance of the specified type or null or undefined if data is null or undefined.
    */
    static convertToType(data, type) {
        if (data === null || data === undefined)
            return data

        switch (type) {
            case 'Boolean':
                return Boolean(data);
            case 'Integer':
                return parseInt(data, 10);
            case 'Number':
                return parseFloat(data);
            case 'String':
                return String(data);
            case 'Date':
                return ApiClient.parseDate(String(data));
            case 'Blob':
                return data;
            default:
                if (type === Object) {
                    // generic object, return directly
                    return data;
                } else if (typeof type.constructFromObject === 'function') {
                    // for model type like User and enum class
                    return type.constructFromObject(data);
                } else if (Array.isArray(type)) {
                    // for array type like: ['String']
                    var itemType = type[0];

                    return data.map((item) => {
                        return ApiClient.convertToType(item, itemType);
                    });
                } else if (typeof type === 'object') {
                    // for plain object type like: {'String': 'Integer'}
                    var keyType, valueType;
                    for (var k in type) {
                        if (type.hasOwnProperty(k)) {
                            keyType = k;
                            valueType = type[k];
                            break;
                        }
                    }

                    var result = {};
                    for (var k in data) {
                        if (data.hasOwnProperty(k)) {
                            var key = ApiClient.convertToType(k, keyType);
                            var value = ApiClient.convertToType(data[k], valueType);
                            result[key] = value;
                        }
                    }

                    return result;
                } else {
                    // for unknown type, return the data directly
                    return data;
                }
        }
    }

  /**
    * Gets an array of host settings
    * @returns An array of host settings
    */
    hostSettings() {
        return [
            {
              'url': "https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5",
              'description': "Sandbox Server",
            },
            {
              'url': "https://services.nbg.gr/apis/open-banking/v3.1.5/aisp",
              'description': "Production Server",
            }
      ];
    }

    getBasePathFromSettings(index, variables={}) {
        var servers = this.hostSettings();

        // check array index out of bound
        if (index < 0 || index >= servers.length) {
            throw new Error("Invalid index " + index + " when selecting the host settings. Must be less than " + servers.length);
        }

        var server = servers[index];
        var url = server['url'];

        // go through variable and assign a value
        for (var variable_name in server['variables']) {
            if (variable_name in variables) {
                let variable = server['variables'][variable_name];
                if ( !('enum_values' in variable) || variable['enum_values'].includes(variables[variable_name]) ) {
                    url = url.replace("{" + variable_name + "}", variables[variable_name]);
                } else {
                    throw new Error("The variable `" + variable_name + "` in the host URL has invalid value " + variables[variable_name] + ". Must be " + server['variables'][variable_name]['enum_values'] + ".");
                }
            } else {
                // use default value
                url = url.replace("{" + variable_name + "}", server['variables'][variable_name]['default_value'])
            }
        }
        return url;
    }

    /**
    * Constructs a new map or array model from REST data.
    * @param data {Object|Array} The REST data.
    * @param obj {Object|Array} The target object or array.
    */
    static constructFromObject(data, obj, itemType) {
        if (Array.isArray(data)) {
            for (var i = 0; i < data.length; i++) {
                if (data.hasOwnProperty(i))
                    obj[i] = ApiClient.convertToType(data[i], itemType);
            }
        } else {
            for (var k in data) {
                if (data.hasOwnProperty(k))
                    obj[k] = ApiClient.convertToType(data[k], itemType);
            }
        }
    };
}

/**
 * Enumeration of collection format separator strategies.
 * @enum {String}
 * @readonly
 */
ApiClient.CollectionFormatEnum = {
    /**
     * Comma-separated values. Value: <code>csv</code>
     * @const
     */
    CSV: ',',

    /**
     * Space-separated values. Value: <code>ssv</code>
     * @const
     */
    SSV: ' ',

    /**
     * Tab-separated values. Value: <code>tsv</code>
     * @const
     */
    TSV: '\t',

    /**
     * Pipe(|)-separated values. Value: <code>pipes</code>
     * @const
     */
    PIPES: '|',

    /**
     * Native array. Value: <code>multi</code>
     * @const
     */
    MULTI: 'multi'
};

/**
* The default API client implementation.
* @type {module:ApiClient}
*/
ApiClient.instance = new ApiClient();
export default ApiClient;
