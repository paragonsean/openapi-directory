/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import A1Gateway from './model/A1Gateway';
import A1Gateway3dsServers from './model/A1Gateway3dsServers';
import A1GatewayAllOfCredentials from './model/A1GatewayAllOfCredentials';
import AML from './model/AML';
import AMLAddressInner from './model/AMLAddressInner';
import AMLAliasesInner from './model/AMLAliasesInner';
import AMLPassportInner from './model/AMLPassportInner';
import AchPlaidFeature from './model/AchPlaidFeature';
import AclInner from './model/AclInner';
import AcquirerName from './model/AcquirerName';
import AddressMatches from './model/AddressMatches';
import Adyen from './model/Adyen';
import AdyenAllOfCredentials from './model/AdyenAllOfCredentials';
import AdyenAllOfSettings from './model/AdyenAllOfSettings';
import Airpay from './model/Airpay';
import AirpayAllOfCredentials from './model/AirpayAllOfCredentials';
import AlternativePaymentInstrument from './model/AlternativePaymentInstrument';
import AlternativePaymentInstrument2 from './model/AlternativePaymentInstrument2';
import AlternativePaymentInstrument2EmbeddedInner from './model/AlternativePaymentInstrument2EmbeddedInner';
import AlternativePaymentInstrument2LinksInner from './model/AlternativePaymentInstrument2LinksInner';
import AlternativePaymentMethods from './model/AlternativePaymentMethods';
import AlternativePaymentToken from './model/AlternativePaymentToken';
import AmexVPC from './model/AmexVPC';
import AmexVPCAllOfCredentials from './model/AmexVPCAllOfCredentials';
import AmexVPCAllOfSettings from './model/AmexVPCAllOfSettings';
import AmountAdjustment from './model/AmountAdjustment';
import ApcoPay from './model/ApcoPay';
import ApcoPayAllOfCredentials from './model/ApcoPayAllOfCredentials';
import ApcoPayAllOfSettings from './model/ApcoPayAllOfSettings';
import ApiKeyScope from './model/ApiKeyScope';
import ApplePayValidation from './model/ApplePayValidation';
import ApplePayValidationAllOfValidationRequest from './model/ApplePayValidationAllOfValidationRequest';
import ApprovalUrlLink from './model/ApprovalUrlLink';
import AsiaPaymentGateway from './model/AsiaPaymentGateway';
import AsiaPaymentGatewayAllOfCredentials from './model/AsiaPaymentGatewayAllOfCredentials';
import AstroPayCard from './model/AstroPayCard';
import AstroPayCardAllOfCredentials from './model/AstroPayCardAllOfCredentials';
import AstroPayCardAllOfSettings from './model/AstroPayCardAllOfSettings';
import Attachment from './model/Attachment';
import AttachmentEmbeddedInner from './model/AttachmentEmbeddedInner';
import AttachmentLinksInner from './model/AttachmentLinksInner';
import AttachmentResourceLink from './model/AttachmentResourceLink';
import AuthTransactionEmbed from './model/AuthTransactionEmbed';
import AuthTransactionLink from './model/AuthTransactionLink';
import AuthenticationOptions from './model/AuthenticationOptions';
import AuthenticationToken from './model/AuthenticationToken';
import AuthenticationTokenMetadata from './model/AuthenticationTokenMetadata';
import AuthorizeNet from './model/AuthorizeNet';
import AuthorizeNetAllOfCredentials from './model/AuthorizeNetAllOfCredentials';
import Auto from './model/Auto';
import BBANInstrument from './model/BBANInstrument';
import BBANType from './model/BBANType';
import Bambora from './model/Bambora';
import BamboraAllOfCredentials from './model/BamboraAllOfCredentials';
import BankAccount from './model/BankAccount';
import BankAccountAllOfEmbedded from './model/BankAccountAllOfEmbedded';
import BankAccountAllOfLinks from './model/BankAccountAllOfLinks';
import BankAccountCreatePlain from './model/BankAccountCreatePlain';
import BankAccountCreateToken from './model/BankAccountCreateToken';
import BankAccountEmbed from './model/BankAccountEmbed';
import BankAccountInstrument from './model/BankAccountInstrument';
import BankAccountToken from './model/BankAccountToken';
import BankAccountUpdatePlain from './model/BankAccountUpdatePlain';
import BitPay from './model/BitPay';
import BitPayAllOfCredentials from './model/BitPayAllOfCredentials';
import BlankProblem from './model/BlankProblem';
import Blocklist from './model/Blocklist';
import BlueSnap from './model/BlueSnap';
import BlueSnapAllOfCredentials from './model/BlueSnapAllOfCredentials';
import BraintreePayments from './model/BraintreePayments';
import BraintreePaymentsAllOfCredentials from './model/BraintreePaymentsAllOfCredentials';
import BrowserData from './model/BrowserData';
import CASHlib from './model/CASHlib';
import CASHlibAllOfCredentials from './model/CASHlibAllOfCredentials';
import CCAvenue from './model/CCAvenue';
import CCAvenueAllOfCredentials from './model/CCAvenueAllOfCredentials';
import CODVoucher from './model/CODVoucher';
import CODVoucherAllOfCredentials from './model/CODVoucherAllOfCredentials';
import CardinalCommerce3dsServer from './model/CardinalCommerce3dsServer';
import Cardknox from './model/Cardknox';
import CardknoxAllOfCredentials from './model/CardknoxAllOfCredentials';
import CashInstrument from './model/CashInstrument';
import CashToCode from './model/CashToCode';
import CashToCodeAllOfCredentials from './model/CashToCodeAllOfCredentials';
import CashToCodeAllOfSettings from './model/CashToCodeAllOfSettings';
import Cashflows from './model/Cashflows';
import CashflowsAllOfCredentials from './model/CashflowsAllOfCredentials';
import CauriPayment from './model/CauriPayment';
import CauriPaymentAllOfCredentials from './model/CauriPaymentAllOfCredentials';
import Cayan from './model/Cayan';
import CayanAllOfCredentials from './model/CayanAllOfCredentials';
import Chase from './model/Chase';
import ChaseAllOfCredentials from './model/ChaseAllOfCredentials';
import CheckInstrument from './model/CheckInstrument';
import Circle from './model/Circle';
import CircleAllOfCredentials from './model/CircleAllOfCredentials';
import Citadel from './model/Citadel';
import CitadelAllOfCredentials from './model/CitadelAllOfCredentials';
import Clearhaus from './model/Clearhaus';
import Clearhaus3dsServer from './model/Clearhaus3dsServer';
import Clearhaus3dsServers from './model/Clearhaus3dsServers';
import ClearhausAllOfCredentials from './model/ClearhausAllOfCredentials';
import CoinPayments from './model/CoinPayments';
import CoinPaymentsAllOfCredentials from './model/CoinPaymentsAllOfCredentials';
import CommonBankAccount from './model/CommonBankAccount';
import CommonInvoice from './model/CommonInvoice';
import CommonKycDocument from './model/CommonKycDocument';
import CommonKycDocumentLinksInner from './model/CommonKycDocumentLinksInner';
import CommonKycRequest from './model/CommonKycRequest';
import CommonKycRequestDocumentsInner from './model/CommonKycRequestDocumentsInner';
import CommonOneTimeOrder from './model/CommonOneTimeOrder';
import CommonPayPalAccount from './model/CommonPayPalAccount';
import CommonPaymentCard from './model/CommonPaymentCard';
import CommonPaymentToken from './model/CommonPaymentToken';
import CommonPlan from './model/CommonPlan';
import CommonPlanRecurringInterval from './model/CommonPlanRecurringInterval';
import CommonPlanSetup from './model/CommonPlanSetup';
import CommonPlanTrial from './model/CommonPlanTrial';
import CommonProduct from './model/CommonProduct';
import CommonScheduleInstruction from './model/CommonScheduleInstruction';
import CommonSubscription from './model/CommonSubscription';
import CommonSubscriptionItemsInner from './model/CommonSubscriptionItemsInner';
import CommonSubscriptionOrder from './model/CommonSubscriptionOrder';
import CommonSubscriptionOrderAllOfLineItemSubtotal from './model/CommonSubscriptionOrderAllOfLineItemSubtotal';
import CommonSubscriptionOrderAllOfRecurringInterval from './model/CommonSubscriptionOrderAllOfRecurringInterval';
import CommonSubscriptionOrderAllOfTrial from './model/CommonSubscriptionOrderAllOfTrial';
import CommonTransaction from './model/CommonTransaction';
import CommonTransactionRequest from './model/CommonTransactionRequest';
import CompositeToken from './model/CompositeToken';
import Conekta from './model/Conekta';
import ConektaAllOfCredentials from './model/ConektaAllOfCredentials';
import ContactEmailsInner from './model/ContactEmailsInner';
import ContactObject from './model/ContactObject';
import ContactPhoneNumbersInner from './model/ContactPhoneNumbersInner';
import Coppr from './model/Coppr';
import CopprAllOfCredentials from './model/CopprAllOfCredentials';
import CopprAllOfSettings from './model/CopprAllOfSettings';
import CoreReadyToPay from './model/CoreReadyToPay';
import Coupon from './model/Coupon';
import CouponExpiration from './model/CouponExpiration';
import CouponRedemption from './model/CouponRedemption';
import CouponRestriction from './model/CouponRestriction';
import Credential from './model/Credential';
import Credorax from './model/Credorax';
import CredoraxAllOfCredentials from './model/CredoraxAllOfCredentials';
import Cryptonator from './model/Cryptonator';
import CryptonatorAllOfCredentials from './model/CryptonatorAllOfCredentials';
import CustomEventScheduleInstruction from './model/CustomEventScheduleInstruction';
import CustomField from './model/CustomField';
import Customer from './model/Customer';
import CustomerAverageValue from './model/CustomerAverageValue';
import CustomerEmbed from './model/CustomerEmbed';
import CustomerEmbeddedInner from './model/CustomerEmbeddedInner';
import CustomerJWT from './model/CustomerJWT';
import CustomerLifetimeRevenue from './model/CustomerLifetimeRevenue';
import CustomerLink from './model/CustomerLink';
import CustomerLinksInner from './model/CustomerLinksInner';
import CustomerTimeline from './model/CustomerTimeline';
import CustomerTimelineCustomEvent from './model/CustomerTimelineCustomEvent';
import CyberSource from './model/CyberSource';
import CyberSourceAllOfCredentials from './model/CyberSourceAllOfCredentials';
import DLocal from './model/DLocal';
import DLocalAllOfCredentials from './model/DLocalAllOfCredentials';
import DLocalAllOfSettings from './model/DLocalAllOfSettings';
import DataCash from './model/DataCash';
import DataCash3dsServer from './model/DataCash3dsServer';
import DataCash3dsServers from './model/DataCash3dsServers';
import DataCashAllOfCredentials from './model/DataCashAllOfCredentials';
import DataCashAllOfSettings from './model/DataCashAllOfSettings';
import DateInterval from './model/DateInterval';
import DateIntervalAllOfUnit from './model/DateIntervalAllOfUnit';
import DayOfMonth from './model/DayOfMonth';
import DayOfWeek from './model/DayOfWeek';
import DayOfWeekLong from './model/DayOfWeekLong';
import DefaultPaymentInstrumentLink from './model/DefaultPaymentInstrumentLink';
import Dengi from './model/Dengi';
import DengiAllOfCredentials from './model/DengiAllOfCredentials';
import DetailedProblem from './model/DetailedProblem';
import DigitalWalletToken from './model/DigitalWalletToken';
import DigitalWalletValidation from './model/DigitalWalletValidation';
import DigitalWallets from './model/DigitalWallets';
import DigitalWalletsApplePay from './model/DigitalWalletsApplePay';
import DigitalWalletsGooglePay from './model/DigitalWalletsGooglePay';
import Directa24 from './model/Directa24';
import Directa24AllOfCredentials from './model/Directa24AllOfCredentials';
import Directa24AllOfSettings from './model/Directa24AllOfSettings';
import Directa24Banks from './model/Directa24Banks';
import Discount from './model/Discount';
import DiscountsPerRedemption from './model/DiscountsPerRedemption';
import Dispute from './model/Dispute';
import DisputeEmbeddedInner from './model/DisputeEmbeddedInner';
import DisputeLink from './model/DisputeLink';
import DisputeLinksInner from './model/DisputeLinksInner';
import DocumentedProblem from './model/DocumentedProblem';
import Dragonphoenix from './model/Dragonphoenix';
import DragonphoenixAllOfCredentials from './model/DragonphoenixAllOfCredentials';
import DueTimeShiftInstruction from './model/DueTimeShiftInstruction';
import DueTimeShiftInstructionUnit from './model/DueTimeShiftInstructionUnit';
import DynamicIpnLink from './model/DynamicIpnLink';
import EBANX from './model/EBANX';
import EBANXAllOfCredentials from './model/EBANXAllOfCredentials';
import EMS from './model/EMS';
import EMS3dsServers from './model/EMS3dsServers';
import EMSAllOfCredentials from './model/EMSAllOfCredentials';
import EMSAllOfSettings from './model/EMSAllOfSettings';
import EMerchantPay from './model/EMerchantPay';
import EMerchantPay3dsServer from './model/EMerchantPay3dsServer';
import EMerchantPay3dsServers from './model/EMerchantPay3dsServers';
import EMerchantPayAllOfCredentials from './model/EMerchantPayAllOfCredentials';
import EMerchantPayAllOfSettings from './model/EMerchantPayAllOfSettings';
import EPG from './model/EPG';
import EPGAllOfCredentials from './model/EPGAllOfCredentials';
import EPro from './model/EPro';
import EProAllOfCredentials from './model/EProAllOfCredentials';
import EZeeWallet from './model/EZeeWallet';
import EZeeWalletAllOfCredentials from './model/EZeeWalletAllOfCredentials';
import EcoPayz from './model/EcoPayz';
import EcoPayzAllOfCredentials from './model/EcoPayzAllOfCredentials';
import EcoPayzAllOfSettings from './model/EcoPayzAllOfSettings';
import EcorePay from './model/EcorePay';
import EcorePayAllOfCredentials from './model/EcorePayAllOfCredentials';
import Elavon from './model/Elavon';
import ElavonAllOfCredentials from './model/ElavonAllOfCredentials';
import Error from './model/Error';
import Euteller from './model/Euteller';
import EutellerAllOfCredentials from './model/EutellerAllOfCredentials';
import EzyEFT from './model/EzyEFT';
import EzyEFTAllOfCredentials from './model/EzyEFTAllOfCredentials';
import File from './model/File';
import FileCreateFromInline from './model/FileCreateFromInline';
import FileCreateFromUrl from './model/FileCreateFromUrl';
import FileDownloadLink from './model/FileDownloadLink';
import FileEmbed from './model/FileEmbed';
import FileLink from './model/FileLink';
import FileLinksInner from './model/FileLinksInner';
import FinTecSystems from './model/FinTecSystems';
import FinTecSystemsAllOfCredentials from './model/FinTecSystemsAllOfCredentials';
import FinTecSystemsAllOfSettings from './model/FinTecSystemsAllOfSettings';
import Finrax from './model/Finrax';
import FinraxAllOfCredentials from './model/FinraxAllOfCredentials';
import FinraxAllOfSettings from './model/FinraxAllOfSettings';
import Fixed from './model/Fixed';
import FixedFee from './model/FixedFee';
import FlatRate from './model/FlatRate';
import Flexepin from './model/Flexepin';
import FlexepinAllOfCredentials from './model/FlexepinAllOfCredentials';
import FlexiblePlan from './model/FlexiblePlan';
import Forte from './model/Forte';
import ForteAllOfCredentials from './model/ForteAllOfCredentials';
import FundSend from './model/FundSend';
import FundSendAllOfCredentials from './model/FundSendAllOfCredentials';
import GET from './model/GET';
import GET3dsServers from './model/GET3dsServers';
import GETAllOfCredentials from './model/GETAllOfCredentials';
import GatewayAccount from './model/GatewayAccount';
import GatewayAccountEmbed from './model/GatewayAccountEmbed';
import GatewayAccountLimit from './model/GatewayAccountLimit';
import GatewayAccountLimitLink from './model/GatewayAccountLimitLink';
import GatewayAccountLink from './model/GatewayAccountLink';
import GatewayAccountLinksInner from './model/GatewayAccountLinksInner';
import GatewayName from './model/GatewayName';
import Gigadat from './model/Gigadat';
import GigadatAllOfCredentials from './model/GigadatAllOfCredentials';
import GigadatAllOfSettings from './model/GigadatAllOfSettings';
import GlobalOne from './model/GlobalOne';
import GlobalOneAllOfCredentials from './model/GlobalOneAllOfCredentials';
import GlobalWebhookEventType from './model/GlobalWebhookEventType';
import Gooney from './model/Gooney';
import GooneyAllOfCredentials from './model/GooneyAllOfCredentials';
import Gpaysafe from './model/Gpaysafe';
import GpaysafeAllOfCredentials from './model/GpaysafeAllOfCredentials';
import Greenbox from './model/Greenbox';
import GreenboxAllOfCredentials from './model/GreenboxAllOfCredentials';
import HiPay from './model/HiPay';
import HiPayAllOfCredentials from './model/HiPayAllOfCredentials';
import IBANInstrument from './model/IBANInstrument';
import IBANType from './model/IBANType';
import ICEPAY from './model/ICEPAY';
import ICEPAYAllOfCredentials from './model/ICEPAYAllOfCredentials';
import ICanPay from './model/ICanPay';
import ICanPayAllOfCredentials from './model/ICanPayAllOfCredentials';
import ICheque from './model/ICheque';
import IChequeAllOfCredentials from './model/IChequeAllOfCredentials';
import IDebit from './model/IDebit';
import IDebitAllOfCredentials from './model/IDebitAllOfCredentials';
import INOVAPAY from './model/INOVAPAY';
import INOVAPAYAllOfCredentials from './model/INOVAPAYAllOfCredentials';
import IdentityMatches from './model/IdentityMatches';
import Ilixium from './model/Ilixium';
import Ilixium3dsServer from './model/Ilixium3dsServer';
import Ilixium3dsServers from './model/Ilixium3dsServers';
import IlixiumAllOfCredentials from './model/IlixiumAllOfCredentials';
import IlixiumAllOfSettings from './model/IlixiumAllOfSettings';
import Immediately from './model/Immediately';
import Ingenico from './model/Ingenico';
import Ingenico3dsServer from './model/Ingenico3dsServer';
import Ingenico3dsServers from './model/Ingenico3dsServers';
import IngenicoAllOfCredentials from './model/IngenicoAllOfCredentials';
import InitialInvoiceEmbed from './model/InitialInvoiceEmbed';
import InitialInvoiceLink from './model/InitialInvoiceLink';
import Inovio from './model/Inovio';
import Inovio3dsServer from './model/Inovio3dsServer';
import Inovio3dsServers from './model/Inovio3dsServers';
import InovioAllOfCredentials from './model/InovioAllOfCredentials';
import InovioAllOfSettings from './model/InovioAllOfSettings';
import InstaDebit from './model/InstaDebit';
import InstaDebitAllOfCredentials from './model/InstaDebitAllOfCredentials';
import InstrumentReference from './model/InstrumentReference';
import Intelligent from './model/Intelligent';
import IntelligentAllOfUnit from './model/IntelligentAllOfUnit';
import Intuit from './model/Intuit';
import IntuitAllOfCredentials from './model/IntuitAllOfCredentials';
import InvalidError from './model/InvalidError';
import Invoice from './model/Invoice';
import InvoiceAllOfEmbedded from './model/InvoiceAllOfEmbedded';
import InvoiceAllOfLinks from './model/InvoiceAllOfLinks';
import InvoiceAllOfRetryInstruction from './model/InvoiceAllOfRetryInstruction';
import InvoiceAllOfRetryInstructionAttempts from './model/InvoiceAllOfRetryInstructionAttempts';
import InvoiceDiscount from './model/InvoiceDiscount';
import InvoiceIssue from './model/InvoiceIssue';
import InvoiceItem from './model/InvoiceItem';
import InvoiceItemEmbeddedInner from './model/InvoiceItemEmbeddedInner';
import InvoiceItemLinksInner from './model/InvoiceItemLinksInner';
import InvoiceLink from './model/InvoiceLink';
import InvoiceReissue from './model/InvoiceReissue';
import InvoiceRetryScheduleInstruction from './model/InvoiceRetryScheduleInstruction';
import InvoiceShipping from './model/InvoiceShipping';
import InvoiceTax from './model/InvoiceTax';
import InvoiceTaxItem from './model/InvoiceTaxItem';
import InvoiceTimeShift from './model/InvoiceTimeShift';
import InvoiceTimeline from './model/InvoiceTimeline';
import InvoiceTransaction from './model/InvoiceTransaction';
import InvoiceTransactionAllocation from './model/InvoiceTransactionAllocation';
import InvoiceTransactionAllocationLinksInner from './model/InvoiceTransactionAllocationLinksInner';
import InvoicesEmbed from './model/InvoicesEmbed';
import InvoicesLink from './model/InvoicesLink';
import IpayOptions from './model/IpayOptions';
import IpayOptionsAllOfCredentials from './model/IpayOptionsAllOfCredentials';
import IpayOptionsAllOfSettings from './model/IpayOptionsAllOfSettings';
import IssueTimeShiftInstruction from './model/IssueTimeShiftInstruction';
import JetPay from './model/JetPay';
import JetPayAllOfCredentials from './model/JetPayAllOfCredentials';
import Jeton from './model/Jeton';
import JetonAllOfCredentials from './model/JetonAllOfCredentials';
import JetonAllOfSettings from './model/JetonAllOfSettings';
import Khelocard from './model/Khelocard';
import KhelocardAllOfCredentials from './model/KhelocardAllOfCredentials';
import KhelocardCard from './model/KhelocardCard';
import KhelocardCardToken from './model/KhelocardCardToken';
import Konnektive from './model/Konnektive';
import KonnektiveAllOfCredentials from './model/KonnektiveAllOfCredentials';
import KonnektiveAllOfSettings from './model/KonnektiveAllOfSettings';
import KycDocument from './model/KycDocument';
import KycDocument2 from './model/KycDocument2';
import KycDocumentLink from './model/KycDocumentLink';
import KycDocumentRejection from './model/KycDocumentRejection';
import KycDocumentSubtypes from './model/KycDocumentSubtypes';
import KycDocumentTypes from './model/KycDocumentTypes';
import KycDocumentsLink from './model/KycDocumentsLink';
import KycGathererLink from './model/KycGathererLink';
import KycRequest from './model/KycRequest';
import KycRequestAllOfLinks from './model/KycRequestAllOfLinks';
import LPG from './model/LPG';
import LPGAllOfCredentials from './model/LPGAllOfCredentials';
import LeadSource from './model/LeadSource';
import LeadSourceData from './model/LeadSourceData';
import LeadSourceEmbed from './model/LeadSourceEmbed';
import LeadSourceLink from './model/LeadSourceLink';
import Link from './model/Link';
import List from './model/List';
import Loonie from './model/Loonie';
import LoonieAllOfCredentials from './model/LoonieAllOfCredentials';
import Manual from './model/Manual';
import Manual2 from './model/Manual2';
import Manual2AllOfItems from './model/Manual2AllOfItems';
import MiFinity from './model/MiFinity';
import MiFinityAllOfCredentials from './model/MiFinityAllOfCredentials';
import MinimumOrderAmount from './model/MinimumOrderAmount';
import Moneris from './model/Moneris';
import MonerisAllOfCredentials from './model/MonerisAllOfCredentials';
import Money from './model/Money';
import MtaPay from './model/MtaPay';
import MtaPayAllOfCredentials from './model/MtaPayAllOfCredentials';
import MtaPayAllOfSettings from './model/MtaPayAllOfSettings';
import MuchBetter from './model/MuchBetter';
import MuchBetterAllOfCredentials from './model/MuchBetterAllOfCredentials';
import MuchBetterAllOfSettings from './model/MuchBetterAllOfSettings';
import MyFatoorah from './model/MyFatoorah';
import MyFatoorahAllOfCredentials from './model/MyFatoorahAllOfCredentials';
import NGenius from './model/NGenius';
import NGenius3dsServer from './model/NGenius3dsServer';
import NGenius3dsServers from './model/NGenius3dsServers';
import NGeniusAllOfCredentials from './model/NGeniusAllOfCredentials';
import NMI from './model/NMI';
import NMI3dsServers from './model/NMI3dsServers';
import NMIAllOfCredentials from './model/NMIAllOfCredentials';
import NMIAllOfSettings from './model/NMIAllOfSettings';
import Neosurf from './model/Neosurf';
import NeosurfAllOfCredentials from './model/NeosurfAllOfCredentials';
import Netbanking from './model/Netbanking';
import NetbankingAllOfCredentials from './model/NetbankingAllOfCredentials';
import Neteller from './model/Neteller';
import NetellerAllOfCredentials from './model/NetellerAllOfCredentials';
import NetellerAllOfSettings from './model/NetellerAllOfSettings';
import NinjaWallet from './model/NinjaWallet';
import NinjaWalletAllOfCredentials from './model/NinjaWalletAllOfCredentials';
import NuaPay from './model/NuaPay';
import NuaPayAllOfCredentials from './model/NuaPayAllOfCredentials';
import OchaPay from './model/OchaPay';
import OchaPayAllOfCredentials from './model/OchaPayAllOfCredentials';
import OnBoardingUrlLink from './model/OnBoardingUrlLink';
import OnRamp from './model/OnRamp';
import OnRampAllOfCredentials from './model/OnRampAllOfCredentials';
import OneColumn from './model/OneColumn';
import OneColumnAllOfData from './model/OneColumnAllOfData';
import OneTimeOrder from './model/OneTimeOrder';
import Onlineueberweisen from './model/Onlineueberweisen';
import OnlineueberweisenAllOfCredentials from './model/OnlineueberweisenAllOfCredentials';
import OnlineueberweisenAllOfSettings from './model/OnlineueberweisenAllOfSettings';
import OrderTimeline from './model/OrderTimeline';
import Organization from './model/Organization';
import OrganizationEmbed from './model/OrganizationEmbed';
import OrganizationLink from './model/OrganizationLink';
import OrganizationQuestionnaire from './model/OrganizationQuestionnaire';
import Other from './model/Other';
import Paay3dsServer from './model/Paay3dsServer';
import Pagsmile from './model/Pagsmile';
import PagsmileAllOfCredentials from './model/PagsmileAllOfCredentials';
import PaidByTime from './model/PaidByTime';
import Panamerican from './model/Panamerican';
import Panamerican3dsServer from './model/Panamerican3dsServer';
import Panamerican3dsServers from './model/Panamerican3dsServers';
import PanamericanAllOfCredentials from './model/PanamericanAllOfCredentials';
import PanamericanAllOfSettings from './model/PanamericanAllOfSettings';
import PandaGateway from './model/PandaGateway';
import PandaGatewayAllOfCredentials from './model/PandaGatewayAllOfCredentials';
import ParamountEft from './model/ParamountEft';
import ParamountEftAllOfCredentials from './model/ParamountEftAllOfCredentials';
import ParamountInterac from './model/ParamountInterac';
import ParamountInteracAllOfCredentials from './model/ParamountInteracAllOfCredentials';
import ParentTransactionEmbed from './model/ParentTransactionEmbed';
import ParentTransactionLink from './model/ParentTransactionLink';
import Partial from './model/Partial';
import Password from './model/Password';
import Passwordless from './model/Passwordless';
import PatchKycRequestRequest from './model/PatchKycRequestRequest';
import PatchPaymentInstrumentRequest from './model/PatchPaymentInstrumentRequest';
import PatchTransactionRequest from './model/PatchTransactionRequest';
import Pay4Fun from './model/Pay4Fun';
import Pay4FunAllOfCredentials from './model/Pay4FunAllOfCredentials';
import PayCash from './model/PayCash';
import PayCashAllOfCredentials from './model/PayCashAllOfCredentials';
import PayClub from './model/PayClub';
import PayClubAllOfCredentials from './model/PayClubAllOfCredentials';
import PayClubAllOfSettings from './model/PayClubAllOfSettings';
import PayPal from './model/PayPal';
import PayPalAccount from './model/PayPalAccount';
import PayPalAccountAllOfEmbedded from './model/PayPalAccountAllOfEmbedded';
import PayPalAccountAllOfLinks from './model/PayPalAccountAllOfLinks';
import PayPalAllOfSettings from './model/PayPalAllOfSettings';
import PayTabs from './model/PayTabs';
import PayTabsAllOfCredentials from './model/PayTabsAllOfCredentials';
import PayULatam from './model/PayULatam';
import PayULatamAllOfCredentials from './model/PayULatamAllOfCredentials';
import Payeezy from './model/Payeezy';
import PayeezyAllOfCredentials from './model/PayeezyAllOfCredentials';
import Payflow from './model/Payflow';
import PayflowAllOfCredentials from './model/PayflowAllOfCredentials';
import PaymenTechnologies from './model/PaymenTechnologies';
import PaymenTechnologiesAllOfCredentials from './model/PaymenTechnologiesAllOfCredentials';
import PaymenTechnologiesAllOfSettings from './model/PaymenTechnologiesAllOfSettings';
import PaymentAsia from './model/PaymentAsia';
import PaymentAsiaAllOfCredentials from './model/PaymentAsiaAllOfCredentials';
import PaymentCard from './model/PaymentCard';
import PaymentCardAllOfEmbedded from './model/PaymentCardAllOfEmbedded';
import PaymentCardAllOfLinks from './model/PaymentCardAllOfLinks';
import PaymentCardBrand from './model/PaymentCardBrand';
import PaymentCardCreatePlain from './model/PaymentCardCreatePlain';
import PaymentCardCreateToken from './model/PaymentCardCreateToken';
import PaymentCardDigitalWalletFeature from './model/PaymentCardDigitalWalletFeature';
import PaymentCardEmbed from './model/PaymentCardEmbed';
import PaymentCardLink from './model/PaymentCardLink';
import PaymentCardToken from './model/PaymentCardToken';
import PaymentCardUpdatePlain from './model/PaymentCardUpdatePlain';
import PaymentInstruction from './model/PaymentInstruction';
import PaymentInstrument from './model/PaymentInstrument';
import PaymentInstrument2 from './model/PaymentInstrument2';
import PaymentInstrument3 from './model/PaymentInstrument3';
import PaymentInstrumentCreateToken from './model/PaymentInstrumentCreateToken';
import PaymentInstrumentUpdateToken from './model/PaymentInstrumentUpdateToken';
import PaymentMethod from './model/PaymentMethod';
import PaymentMethods from './model/PaymentMethods';
import PaymentRetry from './model/PaymentRetry';
import PaymentRetryAttemptsInner from './model/PaymentRetryAttemptsInner';
import PaymentToken from './model/PaymentToken';
import PaymentsOS from './model/PaymentsOS';
import PaymentsOSAllOfCredentials from './model/PaymentsOSAllOfCredentials';
import Paymero from './model/Paymero';
import PaymeroAllOfCredentials from './model/PaymeroAllOfCredentials';
import PaymeroAllOfSettings from './model/PaymeroAllOfSettings';
import PayoutRequest from './model/PayoutRequest';
import Payr from './model/Payr';
import PayrAllOfCredentials from './model/PayrAllOfCredentials';
import Paysafe from './model/Paysafe';
import Paysafe3dsServer from './model/Paysafe3dsServer';
import Paysafe3dsServers from './model/Paysafe3dsServers';
import PaysafeAllOfCredentials from './model/PaysafeAllOfCredentials';
import Paysafecash from './model/Paysafecash';
import PaysafecashAllOfCredentials from './model/PaysafecashAllOfCredentials';
import Payvision from './model/Payvision';
import Payvision3dsServer from './model/Payvision3dsServer';
import Payvision3dsServers from './model/Payvision3dsServers';
import PayvisionAllOfCredentials from './model/PayvisionAllOfCredentials';
import PayvisionAllOfSettings from './model/PayvisionAllOfSettings';
import Percent from './model/Percent';
import PermalinkLink from './model/PermalinkLink';
import Piastrix from './model/Piastrix';
import Piastrix3dsServer from './model/Piastrix3dsServer';
import Piastrix3dsServers from './model/Piastrix3dsServers';
import PiastrixAllOfCredentials from './model/PiastrixAllOfCredentials';
import PiastrixAllOfSettings from './model/PiastrixAllOfSettings';
import PlaidAccountToken from './model/PlaidAccountToken';
import Plan from './model/Plan';
import PlanBillingTiming from './model/PlanBillingTiming';
import PlanEmbed from './model/PlanEmbed';
import PlanPeriod from './model/PlanPeriod';
import PlanPriceFormula from './model/PlanPriceFormula';
import Plugnpay from './model/Plugnpay';
import PlugnpayAllOfCredentials from './model/PlugnpayAllOfCredentials';
import PostBankAccountRequest from './model/PostBankAccountRequest';
import PostFileRequest from './model/PostFileRequest';
import PostFinance from './model/PostFinance';
import PostFinanceAllOfCredentials from './model/PostFinanceAllOfCredentials';
import PostKycDocumentMatchesRequest from './model/PostKycDocumentMatchesRequest';
import PostPaymentCardRequest from './model/PostPaymentCardRequest';
import PostPaymentInstrumentRequest from './model/PostPaymentInstrumentRequest';
import PostTagCustomerCollectionRequest from './model/PostTagCustomerCollectionRequest';
import PriceBasedShippingRate from './model/PriceBasedShippingRate';
import Problem from './model/Problem';
import Product from './model/Product';
import ProductEmbed from './model/ProductEmbed';
import ProductLink from './model/ProductLink';
import ProofOfAddress from './model/ProofOfAddress';
import ProofOfAddressAllOfDocumentMatches from './model/ProofOfAddressAllOfDocumentMatches';
import ProofOfAddressAllOfLinks from './model/ProofOfAddressAllOfLinks';
import ProofOfFunds from './model/ProofOfFunds';
import ProofOfIdentity from './model/ProofOfIdentity';
import ProofOfIdentityAllOfDocumentMatches from './model/ProofOfIdentityAllOfDocumentMatches';
import ProofOfIdentityAllOfLinks from './model/ProofOfIdentityAllOfLinks';
import ProofOfPurchase from './model/ProofOfPurchase';
import Prosa from './model/Prosa';
import ProsaAllOfCredentials from './model/ProsaAllOfCredentials';
import PurchaseBumpOffer from './model/PurchaseBumpOffer';
import PurchaseBumpStatus from './model/PurchaseBumpStatus';
import QueryUrlLink from './model/QueryUrlLink';
import RPN from './model/RPN';
import RPNAllOfCredentials from './model/RPNAllOfCredentials';
import Rapyd from './model/Rapyd';
import RapydAllOfCredentials from './model/RapydAllOfCredentials';
import ReadyToPay from './model/ReadyToPay';
import ReadyToPayAchMethod from './model/ReadyToPayAchMethod';
import ReadyToPayAchMethodFeature from './model/ReadyToPayAchMethodFeature';
import ReadyToPayAmount from './model/ReadyToPayAmount';
import ReadyToPayGenericMethod from './model/ReadyToPayGenericMethod';
import ReadyToPayItems from './model/ReadyToPayItems';
import ReadyToPayItemsItemsInner from './model/ReadyToPayItemsItemsInner';
import ReadyToPayMethodsInner from './model/ReadyToPayMethodsInner';
import ReadyToPayPaymentCardMethod from './model/ReadyToPayPaymentCardMethod';
import ReadyToPayPaymentCardMethodFeature from './model/ReadyToPayPaymentCardMethodFeature';
import Realex from './model/Realex';
import RealexAllOfCredentials from './model/RealexAllOfCredentials';
import Realtime from './model/Realtime';
import RealtimeAllOfCredentials from './model/RealtimeAllOfCredentials';
import Rebilly from './model/Rebilly';
import RebillyTaxjar from './model/RebillyTaxjar';
import RebillyTaxjarAllOfItems from './model/RebillyTaxjarAllOfItems';
import RecalculateInvoiceLink from './model/RecalculateInvoiceLink';
import RecentInvoiceEmbed from './model/RecentInvoiceEmbed';
import RecentInvoiceLink from './model/RecentInvoiceLink';
import RedemptionCancel from './model/RedemptionCancel';
import RedemptionRestriction from './model/RedemptionRestriction';
import RedemptionsPerCustomer from './model/RedemptionsPerCustomer';
import Redsys from './model/Redsys';
import RedsysAllOfCredentials from './model/RedsysAllOfCredentials';
import RefundUrlLink from './model/RefundUrlLink';
import ResendEmail from './model/ResendEmail';
import ResetPasswordToken from './model/ResetPasswordToken';
import RestrictToInvoices from './model/RestrictToInvoices';
import RestrictToPlans from './model/RestrictToPlans';
import RestrictToProducts from './model/RestrictToProducts';
import RestrictToSubscriptions from './model/RestrictToSubscriptions';
import RetriedTransactionEmbed from './model/RetriedTransactionEmbed';
import RetriedTransactionLink from './model/RetriedTransactionLink';
import RiskMetadata from './model/RiskMetadata';
import Rotessa from './model/Rotessa';
import RotessaAllOfCredentials from './model/RotessaAllOfCredentials';
import RotessaAllOfSettings from './model/RotessaAllOfSettings';
import RulesetRestore from './model/RulesetRestore';
import SMSVoucher from './model/SMSVoucher';
import SMSVoucherAllOfCredentials from './model/SMSVoucherAllOfCredentials';
import Sagepay from './model/Sagepay';
import SagepayAllOfCredentials from './model/SagepayAllOfCredentials';
import SaltarPay from './model/SaltarPay';
import SaltarPayAllOfCredentials from './model/SaltarPayAllOfCredentials';
import SeamlessChex from './model/SeamlessChex';
import SeamlessChexAllOfCredentials from './model/SeamlessChexAllOfCredentials';
import Search from './model/Search';
import SecureTrading from './model/SecureTrading';
import SecureTrading3dsServer from './model/SecureTrading3dsServer';
import SecureTrading3dsServers from './model/SecureTrading3dsServers';
import SecureTradingAllOfCredentials from './model/SecureTradingAllOfCredentials';
import SecurionPay from './model/SecurionPay';
import SecurionPay3dsServers from './model/SecurionPay3dsServers';
import SecurionPayAllOfCredentials from './model/SecurionPayAllOfCredentials';
import SelfLink from './model/SelfLink';
import ServicePeriodAnchorInstruction from './model/ServicePeriodAnchorInstruction';
import ShippingZone from './model/ShippingZone';
import SignedLinkLink from './model/SignedLinkLink';
import Skrill from './model/Skrill';
import SkrillAllOfCredentials from './model/SkrillAllOfCredentials';
import SmartInvoice from './model/SmartInvoice';
import SmartInvoice3dsServer from './model/SmartInvoice3dsServer';
import SmartInvoice3dsServers from './model/SmartInvoice3dsServers';
import SmartInvoiceAllOfCredentials from './model/SmartInvoiceAllOfCredentials';
import Sofort from './model/Sofort';
import SofortAllOfCredentials from './model/SofortAllOfCredentials';
import SparkPay from './model/SparkPay';
import SparkPayAllOfCredentials from './model/SparkPayAllOfCredentials';
import Stairstep from './model/Stairstep';
import StairstepAllOfBrackets from './model/StairstepAllOfBrackets';
import StaticGateway from './model/StaticGateway';
import StaticIpnLink from './model/StaticIpnLink';
import Stripe from './model/Stripe';
import Stripe3dsServer from './model/Stripe3dsServer';
import Stripe3dsServers from './model/Stripe3dsServers';
import StripeAllOfSettings from './model/StripeAllOfSettings';
import Subscription from './model/Subscription';
import SubscriptionCancellation from './model/SubscriptionCancellation';
import SubscriptionCancellationState from './model/SubscriptionCancellationState';
import SubscriptionChange from './model/SubscriptionChange';
import SubscriptionChangeItemsInner from './model/SubscriptionChangeItemsInner';
import SubscriptionInvoice from './model/SubscriptionInvoice';
import SubscriptionLink from './model/SubscriptionLink';
import SubscriptionMetadata from './model/SubscriptionMetadata';
import SubscriptionMetadataEmbeddedInner from './model/SubscriptionMetadataEmbeddedInner';
import SubscriptionMetadataLinksInner from './model/SubscriptionMetadataLinksInner';
import SubscriptionOrder from './model/SubscriptionOrder';
import SubscriptionReactivation from './model/SubscriptionReactivation';
import TWINT from './model/TWINT';
import TWINTAllOfCredentials from './model/TWINTAllOfCredentials';
import TWINTAllOfSettings from './model/TWINTAllOfSettings';
import Tag from './model/Tag';
import TestProcessor from './model/TestProcessor';
import TestProcessor3dsServer from './model/TestProcessor3dsServer';
import TestProcessor3dsServers from './model/TestProcessor3dsServers';
import ThreeColumns from './model/ThreeColumns';
import ThreeColumnsAllOfData from './model/ThreeColumnsAllOfData';
import ThreeDSecure from './model/ThreeDSecure';
import ThreeDSecureIO3dsServer from './model/ThreeDSecureIO3dsServer';
import ThreeDSecureResult from './model/ThreeDSecureResult';
import ThreeDSecureServerName from './model/ThreeDSecureServerName';
import Tiered from './model/Tiered';
import TimePluralUnit from './model/TimePluralUnit';
import TimeUnit from './model/TimeUnit';
import TimelineAction from './model/TimelineAction';
import TimelineExtraData from './model/TimelineExtraData';
import TimelineExtraDataAuthor from './model/TimelineExtraDataAuthor';
import TimelineExtraDataLinksInner from './model/TimelineExtraDataLinksInner';
import TimelineTable from './model/TimelineTable';
import ToditoCash from './model/ToditoCash';
import ToditoCashAllOfCredentials from './model/ToditoCashAllOfCredentials';
import TotalRedemptions from './model/TotalRedemptions';
import Transaction from './model/Transaction';
import TransactionAllOfBumpOffer from './model/TransactionAllOfBumpOffer';
import TransactionAllOfDcc from './model/TransactionAllOfDcc';
import TransactionAllOfEmbedded from './model/TransactionAllOfEmbedded';
import TransactionAllOfGateway from './model/TransactionAllOfGateway';
import TransactionAllOfGatewayAvsResponse from './model/TransactionAllOfGatewayAvsResponse';
import TransactionAllOfGatewayCvvResponse from './model/TransactionAllOfGatewayCvvResponse';
import TransactionAllOfGatewayResponse from './model/TransactionAllOfGatewayResponse';
import TransactionAllOfLinks from './model/TransactionAllOfLinks';
import TransactionAllocationsLink from './model/TransactionAllocationsLink';
import TransactionEmbed from './model/TransactionEmbed';
import TransactionLink from './model/TransactionLink';
import TransactionQuery from './model/TransactionQuery';
import TransactionRefund from './model/TransactionRefund';
import TransactionRequest from './model/TransactionRequest';
import TransactionTimeline from './model/TransactionTimeline';
import TransactionUpdate from './model/TransactionUpdate';
import TransactionUpdateUrlLink from './model/TransactionUpdateUrlLink';
import TrustPay from './model/TrustPay';
import TrustPayAllOfCredentials from './model/TrustPayAllOfCredentials';
import Trustly from './model/Trustly';
import TrustlyAllOfCredentials from './model/TrustlyAllOfCredentials';
import TrustsPay from './model/TrustsPay';
import TrustsPayAllOfCredentials from './model/TrustsPayAllOfCredentials';
import TwoColumns from './model/TwoColumns';
import UPayCard from './model/UPayCard';
import UPayCardAllOfCredentials from './model/UPayCardAllOfCredentials';
import UPayCardAllOfSettings from './model/UPayCardAllOfSettings';
import USAePay from './model/USAePay';
import USAePayAllOfCredentials from './model/USAePayAllOfCredentials';
import UpcomingInvoiceItem from './model/UpcomingInvoiceItem';
import VCreditos from './model/VCreditos';
import VCreditosAllOfCredentials from './model/VCreditosAllOfCredentials';
import ValidationErrorExtensions from './model/ValidationErrorExtensions';
import ValidationErrorExtensionsInvalidFieldsInner from './model/ValidationErrorExtensionsInvalidFieldsInner';
import VantivLitle from './model/VantivLitle';
import VantivLitle3dsServers from './model/VantivLitle3dsServers';
import VantivLitleAllOfCredentials from './model/VantivLitleAllOfCredentials';
import VaultedInstrument from './model/VaultedInstrument';
import VegaaH from './model/VegaaH';
import VegaaHAllOfCredentials from './model/VegaaHAllOfCredentials';
import Volume from './model/Volume';
import Wallet88 from './model/Wallet88';
import Wallet88AllOfCredentials from './model/Wallet88AllOfCredentials';
import Walpay from './model/Walpay';
import Walpay3dsServers from './model/Walpay3dsServers';
import WalpayAllOfCredentials from './model/WalpayAllOfCredentials';
import WebsiteEmbed from './model/WebsiteEmbed';
import WebsiteLink from './model/WebsiteLink';
import Wirecard from './model/Wirecard';
import Wirecard3dsServer from './model/Wirecard3dsServer';
import Wirecard3dsServers from './model/Wirecard3dsServers';
import WirecardAllOfCredentials from './model/WirecardAllOfCredentials';
import WorldlineAtosFrankfurt from './model/WorldlineAtosFrankfurt';
import WorldlineAtosFrankfurt3dsServers from './model/WorldlineAtosFrankfurt3dsServers';
import WorldlineAtosFrankfurtAllOfCredentials from './model/WorldlineAtosFrankfurtAllOfCredentials';
import WorldlineAtosFrankfurtAllOfSettings from './model/WorldlineAtosFrankfurtAllOfSettings';
import Worldpay from './model/Worldpay';
import Worldpay3dsServers from './model/Worldpay3dsServers';
import WorldpayAllOfCredentials from './model/WorldpayAllOfCredentials';
import WorldpayAllOfSettings from './model/WorldpayAllOfSettings';
import XPay from './model/XPay';
import XPayAllOfCredentials from './model/XPayAllOfCredentials';
import Zimpler from './model/Zimpler';
import ZimplerAllOfCredentials from './model/ZimplerAllOfCredentials';
import Zotapay from './model/Zotapay';
import ZotapayAllOfCredentials from './model/ZotapayAllOfCredentials';
import AMLApi from './api/AMLApi';
import BankAccountsApi from './api/BankAccountsApi';
import BlocklistsApi from './api/BlocklistsApi';
import Class3DSecureApi from './api/Class3DSecureApi';
import CouponsApi from './api/CouponsApi';
import CustomFieldsApi from './api/CustomFieldsApi';
import CustomerAuthenticationApi from './api/CustomerAuthenticationApi';
import CustomersApi from './api/CustomersApi';
import CustomersTimelineApi from './api/CustomersTimelineApi';
import DisputesApi from './api/DisputesApi';
import FilesApi from './api/FilesApi';
import InvoicesApi from './api/InvoicesApi';
import KYCDocumentsApi from './api/KYCDocumentsApi';
import OrdersApi from './api/OrdersApi';
import PayPalAccountsApi from './api/PayPalAccountsApi';
import PaymentCardsApi from './api/PaymentCardsApi';
import PaymentInstrumentsApi from './api/PaymentInstrumentsApi';
import PaymentTokensApi from './api/PaymentTokensApi';
import PlansApi from './api/PlansApi';
import ProductsApi from './api/ProductsApi';
import SearchApi from './api/SearchApi';
import ShippingZonesApi from './api/ShippingZonesApi';
import TagsApi from './api/TagsApi';
import TransactionsApi from './api/TransactionsApi';


/**
* # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly&#39;s API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &amp;lt;!-- ReDoc-Inject: &amp;lt;security-definitions&amp;gt; --&amp;gt;  # Errors Rebilly follow&#39;s the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/Forbidden\&quot;} /&amp;gt;  ## Conflict &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/Conflict\&quot;} /&amp;gt;  ## NotFound &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/NotFound\&quot;} /&amp;gt;  ## Unauthorized &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/Unauthorized\&quot;} /&amp;gt;  ## ValidationError &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/ValidationError\&quot;} /&amp;gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the &#x60;$client&#x60;. You may do it like this:  &#x60;&#x60;&#x60;php $client &#x3D; new Rebilly\\Client([     &#39;apiKey&#39; &#x3D;&amp;gt; &#39;YourApiKeyHere&#39;,     &#39;baseUrl&#39; &#x3D;&amp;gt; &#39;https://api.rebilly.com&#39;, ]); &#x60;&#x60;&#x60;  # Using filter with collections Rebilly provides collections filtering. You can use &#x60;?filter&#x60; param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with &#x60;:&#x60;: &#x60;?filter&#x3D;firstName:John&#x60;.  - Sub-fields are separated with &#x60;.&#x60;: &#x60;?filter&#x3D;billingAddress.country:US&#x60;.  - Multiple filters are separated with &#x60;;&#x60;: &#x60;?filter&#x3D;firstName:John;lastName:Doe&#x60;. They will be joined with &#x60;AND&#x60; logic. In this example: &#x60;firstName:John&#x60; AND &#x60;lastName:Doe&#x60;.  - You can use multiple values using &#x60;,&#x60; as values separator: &#x60;?filter&#x3D;firstName:John,Bob&#x60;. Multiple values specified for a field will be joined with &#x60;OR&#x60; logic. In this example: &#x60;firstName:John&#x60; OR &#x60;firstName:Bob&#x60;.  - To negate the filter use &#x60;!&#x60;: &#x60;?filter&#x3D;firstName:!John&#x60;. Note that you can negate multiple values like this: &#x60;?filter&#x3D;firstName:!John,!Bob&#x60;. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: &#x60;?filter&#x3D;amount:1..10&#x60;.  - You can use gte (greater than or equals) filter like this: &#x60;?filter&#x3D;amount:1..&#x60;, or lte (less than or equals) than filter like this: &#x60;?filter&#x3D;amount:..10&#x60;. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: &#x60;?filter&#x3D;firstName:@yourListName&#x60;. You can also exclude list values: &#x60;?filter&#x3D;firstName:!@yourListName&#x60;.  - Datetime-based fields accept values formatted using RFC 3339 like this: &#x60;?filter&#x3D;createdTime:2021-02-14T13:30:00Z&#x60;.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use &#x60;?expand&#x60; param on most requests to expand and include embedded objects within the &#x60;_embedded&#x60; property of the response.  The &#x60;_embedded&#x60; property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  &#x60;&#x60;&#x60; ?expand&#x3D;recentInvoice,customer &#x60;&#x60;&#x60;  And in the response, you would see:  &#x60;&#x60;&#x60; \&quot;_embedded\&quot;: [     \&quot;recentInvoice\&quot;: {...},     \&quot;customer\&quot;: {...} ] &#x60;&#x60;&#x60; Expand may be utilitized not only on &#x60;GET&#x60; requests but also on &#x60;PATCH&#x60;, &#x60;POST&#x60;, &#x60;PUT&#x60; requests too.   # Getting started guide  Rebilly&#39;s API has over 300 operations.  That&#39;s more than you&#39;ll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you&#39;ll have sent API requests (via our console) to create a subscription order. .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var RebillyRestApi = require('index'); // See note below*.
* var xxxSvc = new RebillyRestApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new RebillyRestApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new RebillyRestApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new RebillyRestApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2.1
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The A1Gateway model constructor.
     * @property {module:model/A1Gateway}
     */
    A1Gateway,

    /**
     * The A1Gateway3dsServers model constructor.
     * @property {module:model/A1Gateway3dsServers}
     */
    A1Gateway3dsServers,

    /**
     * The A1GatewayAllOfCredentials model constructor.
     * @property {module:model/A1GatewayAllOfCredentials}
     */
    A1GatewayAllOfCredentials,

    /**
     * The AML model constructor.
     * @property {module:model/AML}
     */
    AML,

    /**
     * The AMLAddressInner model constructor.
     * @property {module:model/AMLAddressInner}
     */
    AMLAddressInner,

    /**
     * The AMLAliasesInner model constructor.
     * @property {module:model/AMLAliasesInner}
     */
    AMLAliasesInner,

    /**
     * The AMLPassportInner model constructor.
     * @property {module:model/AMLPassportInner}
     */
    AMLPassportInner,

    /**
     * The AchPlaidFeature model constructor.
     * @property {module:model/AchPlaidFeature}
     */
    AchPlaidFeature,

    /**
     * The AclInner model constructor.
     * @property {module:model/AclInner}
     */
    AclInner,

    /**
     * The AcquirerName model constructor.
     * @property {module:model/AcquirerName}
     */
    AcquirerName,

    /**
     * The AddressMatches model constructor.
     * @property {module:model/AddressMatches}
     */
    AddressMatches,

    /**
     * The Adyen model constructor.
     * @property {module:model/Adyen}
     */
    Adyen,

    /**
     * The AdyenAllOfCredentials model constructor.
     * @property {module:model/AdyenAllOfCredentials}
     */
    AdyenAllOfCredentials,

    /**
     * The AdyenAllOfSettings model constructor.
     * @property {module:model/AdyenAllOfSettings}
     */
    AdyenAllOfSettings,

    /**
     * The Airpay model constructor.
     * @property {module:model/Airpay}
     */
    Airpay,

    /**
     * The AirpayAllOfCredentials model constructor.
     * @property {module:model/AirpayAllOfCredentials}
     */
    AirpayAllOfCredentials,

    /**
     * The AlternativePaymentInstrument model constructor.
     * @property {module:model/AlternativePaymentInstrument}
     */
    AlternativePaymentInstrument,

    /**
     * The AlternativePaymentInstrument2 model constructor.
     * @property {module:model/AlternativePaymentInstrument2}
     */
    AlternativePaymentInstrument2,

    /**
     * The AlternativePaymentInstrument2EmbeddedInner model constructor.
     * @property {module:model/AlternativePaymentInstrument2EmbeddedInner}
     */
    AlternativePaymentInstrument2EmbeddedInner,

    /**
     * The AlternativePaymentInstrument2LinksInner model constructor.
     * @property {module:model/AlternativePaymentInstrument2LinksInner}
     */
    AlternativePaymentInstrument2LinksInner,

    /**
     * The AlternativePaymentMethods model constructor.
     * @property {module:model/AlternativePaymentMethods}
     */
    AlternativePaymentMethods,

    /**
     * The AlternativePaymentToken model constructor.
     * @property {module:model/AlternativePaymentToken}
     */
    AlternativePaymentToken,

    /**
     * The AmexVPC model constructor.
     * @property {module:model/AmexVPC}
     */
    AmexVPC,

    /**
     * The AmexVPCAllOfCredentials model constructor.
     * @property {module:model/AmexVPCAllOfCredentials}
     */
    AmexVPCAllOfCredentials,

    /**
     * The AmexVPCAllOfSettings model constructor.
     * @property {module:model/AmexVPCAllOfSettings}
     */
    AmexVPCAllOfSettings,

    /**
     * The AmountAdjustment model constructor.
     * @property {module:model/AmountAdjustment}
     */
    AmountAdjustment,

    /**
     * The ApcoPay model constructor.
     * @property {module:model/ApcoPay}
     */
    ApcoPay,

    /**
     * The ApcoPayAllOfCredentials model constructor.
     * @property {module:model/ApcoPayAllOfCredentials}
     */
    ApcoPayAllOfCredentials,

    /**
     * The ApcoPayAllOfSettings model constructor.
     * @property {module:model/ApcoPayAllOfSettings}
     */
    ApcoPayAllOfSettings,

    /**
     * The ApiKeyScope model constructor.
     * @property {module:model/ApiKeyScope}
     */
    ApiKeyScope,

    /**
     * The ApplePayValidation model constructor.
     * @property {module:model/ApplePayValidation}
     */
    ApplePayValidation,

    /**
     * The ApplePayValidationAllOfValidationRequest model constructor.
     * @property {module:model/ApplePayValidationAllOfValidationRequest}
     */
    ApplePayValidationAllOfValidationRequest,

    /**
     * The ApprovalUrlLink model constructor.
     * @property {module:model/ApprovalUrlLink}
     */
    ApprovalUrlLink,

    /**
     * The AsiaPaymentGateway model constructor.
     * @property {module:model/AsiaPaymentGateway}
     */
    AsiaPaymentGateway,

    /**
     * The AsiaPaymentGatewayAllOfCredentials model constructor.
     * @property {module:model/AsiaPaymentGatewayAllOfCredentials}
     */
    AsiaPaymentGatewayAllOfCredentials,

    /**
     * The AstroPayCard model constructor.
     * @property {module:model/AstroPayCard}
     */
    AstroPayCard,

    /**
     * The AstroPayCardAllOfCredentials model constructor.
     * @property {module:model/AstroPayCardAllOfCredentials}
     */
    AstroPayCardAllOfCredentials,

    /**
     * The AstroPayCardAllOfSettings model constructor.
     * @property {module:model/AstroPayCardAllOfSettings}
     */
    AstroPayCardAllOfSettings,

    /**
     * The Attachment model constructor.
     * @property {module:model/Attachment}
     */
    Attachment,

    /**
     * The AttachmentEmbeddedInner model constructor.
     * @property {module:model/AttachmentEmbeddedInner}
     */
    AttachmentEmbeddedInner,

    /**
     * The AttachmentLinksInner model constructor.
     * @property {module:model/AttachmentLinksInner}
     */
    AttachmentLinksInner,

    /**
     * The AttachmentResourceLink model constructor.
     * @property {module:model/AttachmentResourceLink}
     */
    AttachmentResourceLink,

    /**
     * The AuthTransactionEmbed model constructor.
     * @property {module:model/AuthTransactionEmbed}
     */
    AuthTransactionEmbed,

    /**
     * The AuthTransactionLink model constructor.
     * @property {module:model/AuthTransactionLink}
     */
    AuthTransactionLink,

    /**
     * The AuthenticationOptions model constructor.
     * @property {module:model/AuthenticationOptions}
     */
    AuthenticationOptions,

    /**
     * The AuthenticationToken model constructor.
     * @property {module:model/AuthenticationToken}
     */
    AuthenticationToken,

    /**
     * The AuthenticationTokenMetadata model constructor.
     * @property {module:model/AuthenticationTokenMetadata}
     */
    AuthenticationTokenMetadata,

    /**
     * The AuthorizeNet model constructor.
     * @property {module:model/AuthorizeNet}
     */
    AuthorizeNet,

    /**
     * The AuthorizeNetAllOfCredentials model constructor.
     * @property {module:model/AuthorizeNetAllOfCredentials}
     */
    AuthorizeNetAllOfCredentials,

    /**
     * The Auto model constructor.
     * @property {module:model/Auto}
     */
    Auto,

    /**
     * The BBANInstrument model constructor.
     * @property {module:model/BBANInstrument}
     */
    BBANInstrument,

    /**
     * The BBANType model constructor.
     * @property {module:model/BBANType}
     */
    BBANType,

    /**
     * The Bambora model constructor.
     * @property {module:model/Bambora}
     */
    Bambora,

    /**
     * The BamboraAllOfCredentials model constructor.
     * @property {module:model/BamboraAllOfCredentials}
     */
    BamboraAllOfCredentials,

    /**
     * The BankAccount model constructor.
     * @property {module:model/BankAccount}
     */
    BankAccount,

    /**
     * The BankAccountAllOfEmbedded model constructor.
     * @property {module:model/BankAccountAllOfEmbedded}
     */
    BankAccountAllOfEmbedded,

    /**
     * The BankAccountAllOfLinks model constructor.
     * @property {module:model/BankAccountAllOfLinks}
     */
    BankAccountAllOfLinks,

    /**
     * The BankAccountCreatePlain model constructor.
     * @property {module:model/BankAccountCreatePlain}
     */
    BankAccountCreatePlain,

    /**
     * The BankAccountCreateToken model constructor.
     * @property {module:model/BankAccountCreateToken}
     */
    BankAccountCreateToken,

    /**
     * The BankAccountEmbed model constructor.
     * @property {module:model/BankAccountEmbed}
     */
    BankAccountEmbed,

    /**
     * The BankAccountInstrument model constructor.
     * @property {module:model/BankAccountInstrument}
     */
    BankAccountInstrument,

    /**
     * The BankAccountToken model constructor.
     * @property {module:model/BankAccountToken}
     */
    BankAccountToken,

    /**
     * The BankAccountUpdatePlain model constructor.
     * @property {module:model/BankAccountUpdatePlain}
     */
    BankAccountUpdatePlain,

    /**
     * The BitPay model constructor.
     * @property {module:model/BitPay}
     */
    BitPay,

    /**
     * The BitPayAllOfCredentials model constructor.
     * @property {module:model/BitPayAllOfCredentials}
     */
    BitPayAllOfCredentials,

    /**
     * The BlankProblem model constructor.
     * @property {module:model/BlankProblem}
     */
    BlankProblem,

    /**
     * The Blocklist model constructor.
     * @property {module:model/Blocklist}
     */
    Blocklist,

    /**
     * The BlueSnap model constructor.
     * @property {module:model/BlueSnap}
     */
    BlueSnap,

    /**
     * The BlueSnapAllOfCredentials model constructor.
     * @property {module:model/BlueSnapAllOfCredentials}
     */
    BlueSnapAllOfCredentials,

    /**
     * The BraintreePayments model constructor.
     * @property {module:model/BraintreePayments}
     */
    BraintreePayments,

    /**
     * The BraintreePaymentsAllOfCredentials model constructor.
     * @property {module:model/BraintreePaymentsAllOfCredentials}
     */
    BraintreePaymentsAllOfCredentials,

    /**
     * The BrowserData model constructor.
     * @property {module:model/BrowserData}
     */
    BrowserData,

    /**
     * The CASHlib model constructor.
     * @property {module:model/CASHlib}
     */
    CASHlib,

    /**
     * The CASHlibAllOfCredentials model constructor.
     * @property {module:model/CASHlibAllOfCredentials}
     */
    CASHlibAllOfCredentials,

    /**
     * The CCAvenue model constructor.
     * @property {module:model/CCAvenue}
     */
    CCAvenue,

    /**
     * The CCAvenueAllOfCredentials model constructor.
     * @property {module:model/CCAvenueAllOfCredentials}
     */
    CCAvenueAllOfCredentials,

    /**
     * The CODVoucher model constructor.
     * @property {module:model/CODVoucher}
     */
    CODVoucher,

    /**
     * The CODVoucherAllOfCredentials model constructor.
     * @property {module:model/CODVoucherAllOfCredentials}
     */
    CODVoucherAllOfCredentials,

    /**
     * The CardinalCommerce3dsServer model constructor.
     * @property {module:model/CardinalCommerce3dsServer}
     */
    CardinalCommerce3dsServer,

    /**
     * The Cardknox model constructor.
     * @property {module:model/Cardknox}
     */
    Cardknox,

    /**
     * The CardknoxAllOfCredentials model constructor.
     * @property {module:model/CardknoxAllOfCredentials}
     */
    CardknoxAllOfCredentials,

    /**
     * The CashInstrument model constructor.
     * @property {module:model/CashInstrument}
     */
    CashInstrument,

    /**
     * The CashToCode model constructor.
     * @property {module:model/CashToCode}
     */
    CashToCode,

    /**
     * The CashToCodeAllOfCredentials model constructor.
     * @property {module:model/CashToCodeAllOfCredentials}
     */
    CashToCodeAllOfCredentials,

    /**
     * The CashToCodeAllOfSettings model constructor.
     * @property {module:model/CashToCodeAllOfSettings}
     */
    CashToCodeAllOfSettings,

    /**
     * The Cashflows model constructor.
     * @property {module:model/Cashflows}
     */
    Cashflows,

    /**
     * The CashflowsAllOfCredentials model constructor.
     * @property {module:model/CashflowsAllOfCredentials}
     */
    CashflowsAllOfCredentials,

    /**
     * The CauriPayment model constructor.
     * @property {module:model/CauriPayment}
     */
    CauriPayment,

    /**
     * The CauriPaymentAllOfCredentials model constructor.
     * @property {module:model/CauriPaymentAllOfCredentials}
     */
    CauriPaymentAllOfCredentials,

    /**
     * The Cayan model constructor.
     * @property {module:model/Cayan}
     */
    Cayan,

    /**
     * The CayanAllOfCredentials model constructor.
     * @property {module:model/CayanAllOfCredentials}
     */
    CayanAllOfCredentials,

    /**
     * The Chase model constructor.
     * @property {module:model/Chase}
     */
    Chase,

    /**
     * The ChaseAllOfCredentials model constructor.
     * @property {module:model/ChaseAllOfCredentials}
     */
    ChaseAllOfCredentials,

    /**
     * The CheckInstrument model constructor.
     * @property {module:model/CheckInstrument}
     */
    CheckInstrument,

    /**
     * The Circle model constructor.
     * @property {module:model/Circle}
     */
    Circle,

    /**
     * The CircleAllOfCredentials model constructor.
     * @property {module:model/CircleAllOfCredentials}
     */
    CircleAllOfCredentials,

    /**
     * The Citadel model constructor.
     * @property {module:model/Citadel}
     */
    Citadel,

    /**
     * The CitadelAllOfCredentials model constructor.
     * @property {module:model/CitadelAllOfCredentials}
     */
    CitadelAllOfCredentials,

    /**
     * The Clearhaus model constructor.
     * @property {module:model/Clearhaus}
     */
    Clearhaus,

    /**
     * The Clearhaus3dsServer model constructor.
     * @property {module:model/Clearhaus3dsServer}
     */
    Clearhaus3dsServer,

    /**
     * The Clearhaus3dsServers model constructor.
     * @property {module:model/Clearhaus3dsServers}
     */
    Clearhaus3dsServers,

    /**
     * The ClearhausAllOfCredentials model constructor.
     * @property {module:model/ClearhausAllOfCredentials}
     */
    ClearhausAllOfCredentials,

    /**
     * The CoinPayments model constructor.
     * @property {module:model/CoinPayments}
     */
    CoinPayments,

    /**
     * The CoinPaymentsAllOfCredentials model constructor.
     * @property {module:model/CoinPaymentsAllOfCredentials}
     */
    CoinPaymentsAllOfCredentials,

    /**
     * The CommonBankAccount model constructor.
     * @property {module:model/CommonBankAccount}
     */
    CommonBankAccount,

    /**
     * The CommonInvoice model constructor.
     * @property {module:model/CommonInvoice}
     */
    CommonInvoice,

    /**
     * The CommonKycDocument model constructor.
     * @property {module:model/CommonKycDocument}
     */
    CommonKycDocument,

    /**
     * The CommonKycDocumentLinksInner model constructor.
     * @property {module:model/CommonKycDocumentLinksInner}
     */
    CommonKycDocumentLinksInner,

    /**
     * The CommonKycRequest model constructor.
     * @property {module:model/CommonKycRequest}
     */
    CommonKycRequest,

    /**
     * The CommonKycRequestDocumentsInner model constructor.
     * @property {module:model/CommonKycRequestDocumentsInner}
     */
    CommonKycRequestDocumentsInner,

    /**
     * The CommonOneTimeOrder model constructor.
     * @property {module:model/CommonOneTimeOrder}
     */
    CommonOneTimeOrder,

    /**
     * The CommonPayPalAccount model constructor.
     * @property {module:model/CommonPayPalAccount}
     */
    CommonPayPalAccount,

    /**
     * The CommonPaymentCard model constructor.
     * @property {module:model/CommonPaymentCard}
     */
    CommonPaymentCard,

    /**
     * The CommonPaymentToken model constructor.
     * @property {module:model/CommonPaymentToken}
     */
    CommonPaymentToken,

    /**
     * The CommonPlan model constructor.
     * @property {module:model/CommonPlan}
     */
    CommonPlan,

    /**
     * The CommonPlanRecurringInterval model constructor.
     * @property {module:model/CommonPlanRecurringInterval}
     */
    CommonPlanRecurringInterval,

    /**
     * The CommonPlanSetup model constructor.
     * @property {module:model/CommonPlanSetup}
     */
    CommonPlanSetup,

    /**
     * The CommonPlanTrial model constructor.
     * @property {module:model/CommonPlanTrial}
     */
    CommonPlanTrial,

    /**
     * The CommonProduct model constructor.
     * @property {module:model/CommonProduct}
     */
    CommonProduct,

    /**
     * The CommonScheduleInstruction model constructor.
     * @property {module:model/CommonScheduleInstruction}
     */
    CommonScheduleInstruction,

    /**
     * The CommonSubscription model constructor.
     * @property {module:model/CommonSubscription}
     */
    CommonSubscription,

    /**
     * The CommonSubscriptionItemsInner model constructor.
     * @property {module:model/CommonSubscriptionItemsInner}
     */
    CommonSubscriptionItemsInner,

    /**
     * The CommonSubscriptionOrder model constructor.
     * @property {module:model/CommonSubscriptionOrder}
     */
    CommonSubscriptionOrder,

    /**
     * The CommonSubscriptionOrderAllOfLineItemSubtotal model constructor.
     * @property {module:model/CommonSubscriptionOrderAllOfLineItemSubtotal}
     */
    CommonSubscriptionOrderAllOfLineItemSubtotal,

    /**
     * The CommonSubscriptionOrderAllOfRecurringInterval model constructor.
     * @property {module:model/CommonSubscriptionOrderAllOfRecurringInterval}
     */
    CommonSubscriptionOrderAllOfRecurringInterval,

    /**
     * The CommonSubscriptionOrderAllOfTrial model constructor.
     * @property {module:model/CommonSubscriptionOrderAllOfTrial}
     */
    CommonSubscriptionOrderAllOfTrial,

    /**
     * The CommonTransaction model constructor.
     * @property {module:model/CommonTransaction}
     */
    CommonTransaction,

    /**
     * The CommonTransactionRequest model constructor.
     * @property {module:model/CommonTransactionRequest}
     */
    CommonTransactionRequest,

    /**
     * The CompositeToken model constructor.
     * @property {module:model/CompositeToken}
     */
    CompositeToken,

    /**
     * The Conekta model constructor.
     * @property {module:model/Conekta}
     */
    Conekta,

    /**
     * The ConektaAllOfCredentials model constructor.
     * @property {module:model/ConektaAllOfCredentials}
     */
    ConektaAllOfCredentials,

    /**
     * The ContactEmailsInner model constructor.
     * @property {module:model/ContactEmailsInner}
     */
    ContactEmailsInner,

    /**
     * The ContactObject model constructor.
     * @property {module:model/ContactObject}
     */
    ContactObject,

    /**
     * The ContactPhoneNumbersInner model constructor.
     * @property {module:model/ContactPhoneNumbersInner}
     */
    ContactPhoneNumbersInner,

    /**
     * The Coppr model constructor.
     * @property {module:model/Coppr}
     */
    Coppr,

    /**
     * The CopprAllOfCredentials model constructor.
     * @property {module:model/CopprAllOfCredentials}
     */
    CopprAllOfCredentials,

    /**
     * The CopprAllOfSettings model constructor.
     * @property {module:model/CopprAllOfSettings}
     */
    CopprAllOfSettings,

    /**
     * The CoreReadyToPay model constructor.
     * @property {module:model/CoreReadyToPay}
     */
    CoreReadyToPay,

    /**
     * The Coupon model constructor.
     * @property {module:model/Coupon}
     */
    Coupon,

    /**
     * The CouponExpiration model constructor.
     * @property {module:model/CouponExpiration}
     */
    CouponExpiration,

    /**
     * The CouponRedemption model constructor.
     * @property {module:model/CouponRedemption}
     */
    CouponRedemption,

    /**
     * The CouponRestriction model constructor.
     * @property {module:model/CouponRestriction}
     */
    CouponRestriction,

    /**
     * The Credential model constructor.
     * @property {module:model/Credential}
     */
    Credential,

    /**
     * The Credorax model constructor.
     * @property {module:model/Credorax}
     */
    Credorax,

    /**
     * The CredoraxAllOfCredentials model constructor.
     * @property {module:model/CredoraxAllOfCredentials}
     */
    CredoraxAllOfCredentials,

    /**
     * The Cryptonator model constructor.
     * @property {module:model/Cryptonator}
     */
    Cryptonator,

    /**
     * The CryptonatorAllOfCredentials model constructor.
     * @property {module:model/CryptonatorAllOfCredentials}
     */
    CryptonatorAllOfCredentials,

    /**
     * The CustomEventScheduleInstruction model constructor.
     * @property {module:model/CustomEventScheduleInstruction}
     */
    CustomEventScheduleInstruction,

    /**
     * The CustomField model constructor.
     * @property {module:model/CustomField}
     */
    CustomField,

    /**
     * The Customer model constructor.
     * @property {module:model/Customer}
     */
    Customer,

    /**
     * The CustomerAverageValue model constructor.
     * @property {module:model/CustomerAverageValue}
     */
    CustomerAverageValue,

    /**
     * The CustomerEmbed model constructor.
     * @property {module:model/CustomerEmbed}
     */
    CustomerEmbed,

    /**
     * The CustomerEmbeddedInner model constructor.
     * @property {module:model/CustomerEmbeddedInner}
     */
    CustomerEmbeddedInner,

    /**
     * The CustomerJWT model constructor.
     * @property {module:model/CustomerJWT}
     */
    CustomerJWT,

    /**
     * The CustomerLifetimeRevenue model constructor.
     * @property {module:model/CustomerLifetimeRevenue}
     */
    CustomerLifetimeRevenue,

    /**
     * The CustomerLink model constructor.
     * @property {module:model/CustomerLink}
     */
    CustomerLink,

    /**
     * The CustomerLinksInner model constructor.
     * @property {module:model/CustomerLinksInner}
     */
    CustomerLinksInner,

    /**
     * The CustomerTimeline model constructor.
     * @property {module:model/CustomerTimeline}
     */
    CustomerTimeline,

    /**
     * The CustomerTimelineCustomEvent model constructor.
     * @property {module:model/CustomerTimelineCustomEvent}
     */
    CustomerTimelineCustomEvent,

    /**
     * The CyberSource model constructor.
     * @property {module:model/CyberSource}
     */
    CyberSource,

    /**
     * The CyberSourceAllOfCredentials model constructor.
     * @property {module:model/CyberSourceAllOfCredentials}
     */
    CyberSourceAllOfCredentials,

    /**
     * The DLocal model constructor.
     * @property {module:model/DLocal}
     */
    DLocal,

    /**
     * The DLocalAllOfCredentials model constructor.
     * @property {module:model/DLocalAllOfCredentials}
     */
    DLocalAllOfCredentials,

    /**
     * The DLocalAllOfSettings model constructor.
     * @property {module:model/DLocalAllOfSettings}
     */
    DLocalAllOfSettings,

    /**
     * The DataCash model constructor.
     * @property {module:model/DataCash}
     */
    DataCash,

    /**
     * The DataCash3dsServer model constructor.
     * @property {module:model/DataCash3dsServer}
     */
    DataCash3dsServer,

    /**
     * The DataCash3dsServers model constructor.
     * @property {module:model/DataCash3dsServers}
     */
    DataCash3dsServers,

    /**
     * The DataCashAllOfCredentials model constructor.
     * @property {module:model/DataCashAllOfCredentials}
     */
    DataCashAllOfCredentials,

    /**
     * The DataCashAllOfSettings model constructor.
     * @property {module:model/DataCashAllOfSettings}
     */
    DataCashAllOfSettings,

    /**
     * The DateInterval model constructor.
     * @property {module:model/DateInterval}
     */
    DateInterval,

    /**
     * The DateIntervalAllOfUnit model constructor.
     * @property {module:model/DateIntervalAllOfUnit}
     */
    DateIntervalAllOfUnit,

    /**
     * The DayOfMonth model constructor.
     * @property {module:model/DayOfMonth}
     */
    DayOfMonth,

    /**
     * The DayOfWeek model constructor.
     * @property {module:model/DayOfWeek}
     */
    DayOfWeek,

    /**
     * The DayOfWeekLong model constructor.
     * @property {module:model/DayOfWeekLong}
     */
    DayOfWeekLong,

    /**
     * The DefaultPaymentInstrumentLink model constructor.
     * @property {module:model/DefaultPaymentInstrumentLink}
     */
    DefaultPaymentInstrumentLink,

    /**
     * The Dengi model constructor.
     * @property {module:model/Dengi}
     */
    Dengi,

    /**
     * The DengiAllOfCredentials model constructor.
     * @property {module:model/DengiAllOfCredentials}
     */
    DengiAllOfCredentials,

    /**
     * The DetailedProblem model constructor.
     * @property {module:model/DetailedProblem}
     */
    DetailedProblem,

    /**
     * The DigitalWalletToken model constructor.
     * @property {module:model/DigitalWalletToken}
     */
    DigitalWalletToken,

    /**
     * The DigitalWalletValidation model constructor.
     * @property {module:model/DigitalWalletValidation}
     */
    DigitalWalletValidation,

    /**
     * The DigitalWallets model constructor.
     * @property {module:model/DigitalWallets}
     */
    DigitalWallets,

    /**
     * The DigitalWalletsApplePay model constructor.
     * @property {module:model/DigitalWalletsApplePay}
     */
    DigitalWalletsApplePay,

    /**
     * The DigitalWalletsGooglePay model constructor.
     * @property {module:model/DigitalWalletsGooglePay}
     */
    DigitalWalletsGooglePay,

    /**
     * The Directa24 model constructor.
     * @property {module:model/Directa24}
     */
    Directa24,

    /**
     * The Directa24AllOfCredentials model constructor.
     * @property {module:model/Directa24AllOfCredentials}
     */
    Directa24AllOfCredentials,

    /**
     * The Directa24AllOfSettings model constructor.
     * @property {module:model/Directa24AllOfSettings}
     */
    Directa24AllOfSettings,

    /**
     * The Directa24Banks model constructor.
     * @property {module:model/Directa24Banks}
     */
    Directa24Banks,

    /**
     * The Discount model constructor.
     * @property {module:model/Discount}
     */
    Discount,

    /**
     * The DiscountsPerRedemption model constructor.
     * @property {module:model/DiscountsPerRedemption}
     */
    DiscountsPerRedemption,

    /**
     * The Dispute model constructor.
     * @property {module:model/Dispute}
     */
    Dispute,

    /**
     * The DisputeEmbeddedInner model constructor.
     * @property {module:model/DisputeEmbeddedInner}
     */
    DisputeEmbeddedInner,

    /**
     * The DisputeLink model constructor.
     * @property {module:model/DisputeLink}
     */
    DisputeLink,

    /**
     * The DisputeLinksInner model constructor.
     * @property {module:model/DisputeLinksInner}
     */
    DisputeLinksInner,

    /**
     * The DocumentedProblem model constructor.
     * @property {module:model/DocumentedProblem}
     */
    DocumentedProblem,

    /**
     * The Dragonphoenix model constructor.
     * @property {module:model/Dragonphoenix}
     */
    Dragonphoenix,

    /**
     * The DragonphoenixAllOfCredentials model constructor.
     * @property {module:model/DragonphoenixAllOfCredentials}
     */
    DragonphoenixAllOfCredentials,

    /**
     * The DueTimeShiftInstruction model constructor.
     * @property {module:model/DueTimeShiftInstruction}
     */
    DueTimeShiftInstruction,

    /**
     * The DueTimeShiftInstructionUnit model constructor.
     * @property {module:model/DueTimeShiftInstructionUnit}
     */
    DueTimeShiftInstructionUnit,

    /**
     * The DynamicIpnLink model constructor.
     * @property {module:model/DynamicIpnLink}
     */
    DynamicIpnLink,

    /**
     * The EBANX model constructor.
     * @property {module:model/EBANX}
     */
    EBANX,

    /**
     * The EBANXAllOfCredentials model constructor.
     * @property {module:model/EBANXAllOfCredentials}
     */
    EBANXAllOfCredentials,

    /**
     * The EMS model constructor.
     * @property {module:model/EMS}
     */
    EMS,

    /**
     * The EMS3dsServers model constructor.
     * @property {module:model/EMS3dsServers}
     */
    EMS3dsServers,

    /**
     * The EMSAllOfCredentials model constructor.
     * @property {module:model/EMSAllOfCredentials}
     */
    EMSAllOfCredentials,

    /**
     * The EMSAllOfSettings model constructor.
     * @property {module:model/EMSAllOfSettings}
     */
    EMSAllOfSettings,

    /**
     * The EMerchantPay model constructor.
     * @property {module:model/EMerchantPay}
     */
    EMerchantPay,

    /**
     * The EMerchantPay3dsServer model constructor.
     * @property {module:model/EMerchantPay3dsServer}
     */
    EMerchantPay3dsServer,

    /**
     * The EMerchantPay3dsServers model constructor.
     * @property {module:model/EMerchantPay3dsServers}
     */
    EMerchantPay3dsServers,

    /**
     * The EMerchantPayAllOfCredentials model constructor.
     * @property {module:model/EMerchantPayAllOfCredentials}
     */
    EMerchantPayAllOfCredentials,

    /**
     * The EMerchantPayAllOfSettings model constructor.
     * @property {module:model/EMerchantPayAllOfSettings}
     */
    EMerchantPayAllOfSettings,

    /**
     * The EPG model constructor.
     * @property {module:model/EPG}
     */
    EPG,

    /**
     * The EPGAllOfCredentials model constructor.
     * @property {module:model/EPGAllOfCredentials}
     */
    EPGAllOfCredentials,

    /**
     * The EPro model constructor.
     * @property {module:model/EPro}
     */
    EPro,

    /**
     * The EProAllOfCredentials model constructor.
     * @property {module:model/EProAllOfCredentials}
     */
    EProAllOfCredentials,

    /**
     * The EZeeWallet model constructor.
     * @property {module:model/EZeeWallet}
     */
    EZeeWallet,

    /**
     * The EZeeWalletAllOfCredentials model constructor.
     * @property {module:model/EZeeWalletAllOfCredentials}
     */
    EZeeWalletAllOfCredentials,

    /**
     * The EcoPayz model constructor.
     * @property {module:model/EcoPayz}
     */
    EcoPayz,

    /**
     * The EcoPayzAllOfCredentials model constructor.
     * @property {module:model/EcoPayzAllOfCredentials}
     */
    EcoPayzAllOfCredentials,

    /**
     * The EcoPayzAllOfSettings model constructor.
     * @property {module:model/EcoPayzAllOfSettings}
     */
    EcoPayzAllOfSettings,

    /**
     * The EcorePay model constructor.
     * @property {module:model/EcorePay}
     */
    EcorePay,

    /**
     * The EcorePayAllOfCredentials model constructor.
     * @property {module:model/EcorePayAllOfCredentials}
     */
    EcorePayAllOfCredentials,

    /**
     * The Elavon model constructor.
     * @property {module:model/Elavon}
     */
    Elavon,

    /**
     * The ElavonAllOfCredentials model constructor.
     * @property {module:model/ElavonAllOfCredentials}
     */
    ElavonAllOfCredentials,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The Euteller model constructor.
     * @property {module:model/Euteller}
     */
    Euteller,

    /**
     * The EutellerAllOfCredentials model constructor.
     * @property {module:model/EutellerAllOfCredentials}
     */
    EutellerAllOfCredentials,

    /**
     * The EzyEFT model constructor.
     * @property {module:model/EzyEFT}
     */
    EzyEFT,

    /**
     * The EzyEFTAllOfCredentials model constructor.
     * @property {module:model/EzyEFTAllOfCredentials}
     */
    EzyEFTAllOfCredentials,

    /**
     * The File model constructor.
     * @property {module:model/File}
     */
    File,

    /**
     * The FileCreateFromInline model constructor.
     * @property {module:model/FileCreateFromInline}
     */
    FileCreateFromInline,

    /**
     * The FileCreateFromUrl model constructor.
     * @property {module:model/FileCreateFromUrl}
     */
    FileCreateFromUrl,

    /**
     * The FileDownloadLink model constructor.
     * @property {module:model/FileDownloadLink}
     */
    FileDownloadLink,

    /**
     * The FileEmbed model constructor.
     * @property {module:model/FileEmbed}
     */
    FileEmbed,

    /**
     * The FileLink model constructor.
     * @property {module:model/FileLink}
     */
    FileLink,

    /**
     * The FileLinksInner model constructor.
     * @property {module:model/FileLinksInner}
     */
    FileLinksInner,

    /**
     * The FinTecSystems model constructor.
     * @property {module:model/FinTecSystems}
     */
    FinTecSystems,

    /**
     * The FinTecSystemsAllOfCredentials model constructor.
     * @property {module:model/FinTecSystemsAllOfCredentials}
     */
    FinTecSystemsAllOfCredentials,

    /**
     * The FinTecSystemsAllOfSettings model constructor.
     * @property {module:model/FinTecSystemsAllOfSettings}
     */
    FinTecSystemsAllOfSettings,

    /**
     * The Finrax model constructor.
     * @property {module:model/Finrax}
     */
    Finrax,

    /**
     * The FinraxAllOfCredentials model constructor.
     * @property {module:model/FinraxAllOfCredentials}
     */
    FinraxAllOfCredentials,

    /**
     * The FinraxAllOfSettings model constructor.
     * @property {module:model/FinraxAllOfSettings}
     */
    FinraxAllOfSettings,

    /**
     * The Fixed model constructor.
     * @property {module:model/Fixed}
     */
    Fixed,

    /**
     * The FixedFee model constructor.
     * @property {module:model/FixedFee}
     */
    FixedFee,

    /**
     * The FlatRate model constructor.
     * @property {module:model/FlatRate}
     */
    FlatRate,

    /**
     * The Flexepin model constructor.
     * @property {module:model/Flexepin}
     */
    Flexepin,

    /**
     * The FlexepinAllOfCredentials model constructor.
     * @property {module:model/FlexepinAllOfCredentials}
     */
    FlexepinAllOfCredentials,

    /**
     * The FlexiblePlan model constructor.
     * @property {module:model/FlexiblePlan}
     */
    FlexiblePlan,

    /**
     * The Forte model constructor.
     * @property {module:model/Forte}
     */
    Forte,

    /**
     * The ForteAllOfCredentials model constructor.
     * @property {module:model/ForteAllOfCredentials}
     */
    ForteAllOfCredentials,

    /**
     * The FundSend model constructor.
     * @property {module:model/FundSend}
     */
    FundSend,

    /**
     * The FundSendAllOfCredentials model constructor.
     * @property {module:model/FundSendAllOfCredentials}
     */
    FundSendAllOfCredentials,

    /**
     * The GET model constructor.
     * @property {module:model/GET}
     */
    GET,

    /**
     * The GET3dsServers model constructor.
     * @property {module:model/GET3dsServers}
     */
    GET3dsServers,

    /**
     * The GETAllOfCredentials model constructor.
     * @property {module:model/GETAllOfCredentials}
     */
    GETAllOfCredentials,

    /**
     * The GatewayAccount model constructor.
     * @property {module:model/GatewayAccount}
     */
    GatewayAccount,

    /**
     * The GatewayAccountEmbed model constructor.
     * @property {module:model/GatewayAccountEmbed}
     */
    GatewayAccountEmbed,

    /**
     * The GatewayAccountLimit model constructor.
     * @property {module:model/GatewayAccountLimit}
     */
    GatewayAccountLimit,

    /**
     * The GatewayAccountLimitLink model constructor.
     * @property {module:model/GatewayAccountLimitLink}
     */
    GatewayAccountLimitLink,

    /**
     * The GatewayAccountLink model constructor.
     * @property {module:model/GatewayAccountLink}
     */
    GatewayAccountLink,

    /**
     * The GatewayAccountLinksInner model constructor.
     * @property {module:model/GatewayAccountLinksInner}
     */
    GatewayAccountLinksInner,

    /**
     * The GatewayName model constructor.
     * @property {module:model/GatewayName}
     */
    GatewayName,

    /**
     * The Gigadat model constructor.
     * @property {module:model/Gigadat}
     */
    Gigadat,

    /**
     * The GigadatAllOfCredentials model constructor.
     * @property {module:model/GigadatAllOfCredentials}
     */
    GigadatAllOfCredentials,

    /**
     * The GigadatAllOfSettings model constructor.
     * @property {module:model/GigadatAllOfSettings}
     */
    GigadatAllOfSettings,

    /**
     * The GlobalOne model constructor.
     * @property {module:model/GlobalOne}
     */
    GlobalOne,

    /**
     * The GlobalOneAllOfCredentials model constructor.
     * @property {module:model/GlobalOneAllOfCredentials}
     */
    GlobalOneAllOfCredentials,

    /**
     * The GlobalWebhookEventType model constructor.
     * @property {module:model/GlobalWebhookEventType}
     */
    GlobalWebhookEventType,

    /**
     * The Gooney model constructor.
     * @property {module:model/Gooney}
     */
    Gooney,

    /**
     * The GooneyAllOfCredentials model constructor.
     * @property {module:model/GooneyAllOfCredentials}
     */
    GooneyAllOfCredentials,

    /**
     * The Gpaysafe model constructor.
     * @property {module:model/Gpaysafe}
     */
    Gpaysafe,

    /**
     * The GpaysafeAllOfCredentials model constructor.
     * @property {module:model/GpaysafeAllOfCredentials}
     */
    GpaysafeAllOfCredentials,

    /**
     * The Greenbox model constructor.
     * @property {module:model/Greenbox}
     */
    Greenbox,

    /**
     * The GreenboxAllOfCredentials model constructor.
     * @property {module:model/GreenboxAllOfCredentials}
     */
    GreenboxAllOfCredentials,

    /**
     * The HiPay model constructor.
     * @property {module:model/HiPay}
     */
    HiPay,

    /**
     * The HiPayAllOfCredentials model constructor.
     * @property {module:model/HiPayAllOfCredentials}
     */
    HiPayAllOfCredentials,

    /**
     * The IBANInstrument model constructor.
     * @property {module:model/IBANInstrument}
     */
    IBANInstrument,

    /**
     * The IBANType model constructor.
     * @property {module:model/IBANType}
     */
    IBANType,

    /**
     * The ICEPAY model constructor.
     * @property {module:model/ICEPAY}
     */
    ICEPAY,

    /**
     * The ICEPAYAllOfCredentials model constructor.
     * @property {module:model/ICEPAYAllOfCredentials}
     */
    ICEPAYAllOfCredentials,

    /**
     * The ICanPay model constructor.
     * @property {module:model/ICanPay}
     */
    ICanPay,

    /**
     * The ICanPayAllOfCredentials model constructor.
     * @property {module:model/ICanPayAllOfCredentials}
     */
    ICanPayAllOfCredentials,

    /**
     * The ICheque model constructor.
     * @property {module:model/ICheque}
     */
    ICheque,

    /**
     * The IChequeAllOfCredentials model constructor.
     * @property {module:model/IChequeAllOfCredentials}
     */
    IChequeAllOfCredentials,

    /**
     * The IDebit model constructor.
     * @property {module:model/IDebit}
     */
    IDebit,

    /**
     * The IDebitAllOfCredentials model constructor.
     * @property {module:model/IDebitAllOfCredentials}
     */
    IDebitAllOfCredentials,

    /**
     * The INOVAPAY model constructor.
     * @property {module:model/INOVAPAY}
     */
    INOVAPAY,

    /**
     * The INOVAPAYAllOfCredentials model constructor.
     * @property {module:model/INOVAPAYAllOfCredentials}
     */
    INOVAPAYAllOfCredentials,

    /**
     * The IdentityMatches model constructor.
     * @property {module:model/IdentityMatches}
     */
    IdentityMatches,

    /**
     * The Ilixium model constructor.
     * @property {module:model/Ilixium}
     */
    Ilixium,

    /**
     * The Ilixium3dsServer model constructor.
     * @property {module:model/Ilixium3dsServer}
     */
    Ilixium3dsServer,

    /**
     * The Ilixium3dsServers model constructor.
     * @property {module:model/Ilixium3dsServers}
     */
    Ilixium3dsServers,

    /**
     * The IlixiumAllOfCredentials model constructor.
     * @property {module:model/IlixiumAllOfCredentials}
     */
    IlixiumAllOfCredentials,

    /**
     * The IlixiumAllOfSettings model constructor.
     * @property {module:model/IlixiumAllOfSettings}
     */
    IlixiumAllOfSettings,

    /**
     * The Immediately model constructor.
     * @property {module:model/Immediately}
     */
    Immediately,

    /**
     * The Ingenico model constructor.
     * @property {module:model/Ingenico}
     */
    Ingenico,

    /**
     * The Ingenico3dsServer model constructor.
     * @property {module:model/Ingenico3dsServer}
     */
    Ingenico3dsServer,

    /**
     * The Ingenico3dsServers model constructor.
     * @property {module:model/Ingenico3dsServers}
     */
    Ingenico3dsServers,

    /**
     * The IngenicoAllOfCredentials model constructor.
     * @property {module:model/IngenicoAllOfCredentials}
     */
    IngenicoAllOfCredentials,

    /**
     * The InitialInvoiceEmbed model constructor.
     * @property {module:model/InitialInvoiceEmbed}
     */
    InitialInvoiceEmbed,

    /**
     * The InitialInvoiceLink model constructor.
     * @property {module:model/InitialInvoiceLink}
     */
    InitialInvoiceLink,

    /**
     * The Inovio model constructor.
     * @property {module:model/Inovio}
     */
    Inovio,

    /**
     * The Inovio3dsServer model constructor.
     * @property {module:model/Inovio3dsServer}
     */
    Inovio3dsServer,

    /**
     * The Inovio3dsServers model constructor.
     * @property {module:model/Inovio3dsServers}
     */
    Inovio3dsServers,

    /**
     * The InovioAllOfCredentials model constructor.
     * @property {module:model/InovioAllOfCredentials}
     */
    InovioAllOfCredentials,

    /**
     * The InovioAllOfSettings model constructor.
     * @property {module:model/InovioAllOfSettings}
     */
    InovioAllOfSettings,

    /**
     * The InstaDebit model constructor.
     * @property {module:model/InstaDebit}
     */
    InstaDebit,

    /**
     * The InstaDebitAllOfCredentials model constructor.
     * @property {module:model/InstaDebitAllOfCredentials}
     */
    InstaDebitAllOfCredentials,

    /**
     * The InstrumentReference model constructor.
     * @property {module:model/InstrumentReference}
     */
    InstrumentReference,

    /**
     * The Intelligent model constructor.
     * @property {module:model/Intelligent}
     */
    Intelligent,

    /**
     * The IntelligentAllOfUnit model constructor.
     * @property {module:model/IntelligentAllOfUnit}
     */
    IntelligentAllOfUnit,

    /**
     * The Intuit model constructor.
     * @property {module:model/Intuit}
     */
    Intuit,

    /**
     * The IntuitAllOfCredentials model constructor.
     * @property {module:model/IntuitAllOfCredentials}
     */
    IntuitAllOfCredentials,

    /**
     * The InvalidError model constructor.
     * @property {module:model/InvalidError}
     */
    InvalidError,

    /**
     * The Invoice model constructor.
     * @property {module:model/Invoice}
     */
    Invoice,

    /**
     * The InvoiceAllOfEmbedded model constructor.
     * @property {module:model/InvoiceAllOfEmbedded}
     */
    InvoiceAllOfEmbedded,

    /**
     * The InvoiceAllOfLinks model constructor.
     * @property {module:model/InvoiceAllOfLinks}
     */
    InvoiceAllOfLinks,

    /**
     * The InvoiceAllOfRetryInstruction model constructor.
     * @property {module:model/InvoiceAllOfRetryInstruction}
     */
    InvoiceAllOfRetryInstruction,

    /**
     * The InvoiceAllOfRetryInstructionAttempts model constructor.
     * @property {module:model/InvoiceAllOfRetryInstructionAttempts}
     */
    InvoiceAllOfRetryInstructionAttempts,

    /**
     * The InvoiceDiscount model constructor.
     * @property {module:model/InvoiceDiscount}
     */
    InvoiceDiscount,

    /**
     * The InvoiceIssue model constructor.
     * @property {module:model/InvoiceIssue}
     */
    InvoiceIssue,

    /**
     * The InvoiceItem model constructor.
     * @property {module:model/InvoiceItem}
     */
    InvoiceItem,

    /**
     * The InvoiceItemEmbeddedInner model constructor.
     * @property {module:model/InvoiceItemEmbeddedInner}
     */
    InvoiceItemEmbeddedInner,

    /**
     * The InvoiceItemLinksInner model constructor.
     * @property {module:model/InvoiceItemLinksInner}
     */
    InvoiceItemLinksInner,

    /**
     * The InvoiceLink model constructor.
     * @property {module:model/InvoiceLink}
     */
    InvoiceLink,

    /**
     * The InvoiceReissue model constructor.
     * @property {module:model/InvoiceReissue}
     */
    InvoiceReissue,

    /**
     * The InvoiceRetryScheduleInstruction model constructor.
     * @property {module:model/InvoiceRetryScheduleInstruction}
     */
    InvoiceRetryScheduleInstruction,

    /**
     * The InvoiceShipping model constructor.
     * @property {module:model/InvoiceShipping}
     */
    InvoiceShipping,

    /**
     * The InvoiceTax model constructor.
     * @property {module:model/InvoiceTax}
     */
    InvoiceTax,

    /**
     * The InvoiceTaxItem model constructor.
     * @property {module:model/InvoiceTaxItem}
     */
    InvoiceTaxItem,

    /**
     * The InvoiceTimeShift model constructor.
     * @property {module:model/InvoiceTimeShift}
     */
    InvoiceTimeShift,

    /**
     * The InvoiceTimeline model constructor.
     * @property {module:model/InvoiceTimeline}
     */
    InvoiceTimeline,

    /**
     * The InvoiceTransaction model constructor.
     * @property {module:model/InvoiceTransaction}
     */
    InvoiceTransaction,

    /**
     * The InvoiceTransactionAllocation model constructor.
     * @property {module:model/InvoiceTransactionAllocation}
     */
    InvoiceTransactionAllocation,

    /**
     * The InvoiceTransactionAllocationLinksInner model constructor.
     * @property {module:model/InvoiceTransactionAllocationLinksInner}
     */
    InvoiceTransactionAllocationLinksInner,

    /**
     * The InvoicesEmbed model constructor.
     * @property {module:model/InvoicesEmbed}
     */
    InvoicesEmbed,

    /**
     * The InvoicesLink model constructor.
     * @property {module:model/InvoicesLink}
     */
    InvoicesLink,

    /**
     * The IpayOptions model constructor.
     * @property {module:model/IpayOptions}
     */
    IpayOptions,

    /**
     * The IpayOptionsAllOfCredentials model constructor.
     * @property {module:model/IpayOptionsAllOfCredentials}
     */
    IpayOptionsAllOfCredentials,

    /**
     * The IpayOptionsAllOfSettings model constructor.
     * @property {module:model/IpayOptionsAllOfSettings}
     */
    IpayOptionsAllOfSettings,

    /**
     * The IssueTimeShiftInstruction model constructor.
     * @property {module:model/IssueTimeShiftInstruction}
     */
    IssueTimeShiftInstruction,

    /**
     * The JetPay model constructor.
     * @property {module:model/JetPay}
     */
    JetPay,

    /**
     * The JetPayAllOfCredentials model constructor.
     * @property {module:model/JetPayAllOfCredentials}
     */
    JetPayAllOfCredentials,

    /**
     * The Jeton model constructor.
     * @property {module:model/Jeton}
     */
    Jeton,

    /**
     * The JetonAllOfCredentials model constructor.
     * @property {module:model/JetonAllOfCredentials}
     */
    JetonAllOfCredentials,

    /**
     * The JetonAllOfSettings model constructor.
     * @property {module:model/JetonAllOfSettings}
     */
    JetonAllOfSettings,

    /**
     * The Khelocard model constructor.
     * @property {module:model/Khelocard}
     */
    Khelocard,

    /**
     * The KhelocardAllOfCredentials model constructor.
     * @property {module:model/KhelocardAllOfCredentials}
     */
    KhelocardAllOfCredentials,

    /**
     * The KhelocardCard model constructor.
     * @property {module:model/KhelocardCard}
     */
    KhelocardCard,

    /**
     * The KhelocardCardToken model constructor.
     * @property {module:model/KhelocardCardToken}
     */
    KhelocardCardToken,

    /**
     * The Konnektive model constructor.
     * @property {module:model/Konnektive}
     */
    Konnektive,

    /**
     * The KonnektiveAllOfCredentials model constructor.
     * @property {module:model/KonnektiveAllOfCredentials}
     */
    KonnektiveAllOfCredentials,

    /**
     * The KonnektiveAllOfSettings model constructor.
     * @property {module:model/KonnektiveAllOfSettings}
     */
    KonnektiveAllOfSettings,

    /**
     * The KycDocument model constructor.
     * @property {module:model/KycDocument}
     */
    KycDocument,

    /**
     * The KycDocument2 model constructor.
     * @property {module:model/KycDocument2}
     */
    KycDocument2,

    /**
     * The KycDocumentLink model constructor.
     * @property {module:model/KycDocumentLink}
     */
    KycDocumentLink,

    /**
     * The KycDocumentRejection model constructor.
     * @property {module:model/KycDocumentRejection}
     */
    KycDocumentRejection,

    /**
     * The KycDocumentSubtypes model constructor.
     * @property {module:model/KycDocumentSubtypes}
     */
    KycDocumentSubtypes,

    /**
     * The KycDocumentTypes model constructor.
     * @property {module:model/KycDocumentTypes}
     */
    KycDocumentTypes,

    /**
     * The KycDocumentsLink model constructor.
     * @property {module:model/KycDocumentsLink}
     */
    KycDocumentsLink,

    /**
     * The KycGathererLink model constructor.
     * @property {module:model/KycGathererLink}
     */
    KycGathererLink,

    /**
     * The KycRequest model constructor.
     * @property {module:model/KycRequest}
     */
    KycRequest,

    /**
     * The KycRequestAllOfLinks model constructor.
     * @property {module:model/KycRequestAllOfLinks}
     */
    KycRequestAllOfLinks,

    /**
     * The LPG model constructor.
     * @property {module:model/LPG}
     */
    LPG,

    /**
     * The LPGAllOfCredentials model constructor.
     * @property {module:model/LPGAllOfCredentials}
     */
    LPGAllOfCredentials,

    /**
     * The LeadSource model constructor.
     * @property {module:model/LeadSource}
     */
    LeadSource,

    /**
     * The LeadSourceData model constructor.
     * @property {module:model/LeadSourceData}
     */
    LeadSourceData,

    /**
     * The LeadSourceEmbed model constructor.
     * @property {module:model/LeadSourceEmbed}
     */
    LeadSourceEmbed,

    /**
     * The LeadSourceLink model constructor.
     * @property {module:model/LeadSourceLink}
     */
    LeadSourceLink,

    /**
     * The Link model constructor.
     * @property {module:model/Link}
     */
    Link,

    /**
     * The List model constructor.
     * @property {module:model/List}
     */
    List,

    /**
     * The Loonie model constructor.
     * @property {module:model/Loonie}
     */
    Loonie,

    /**
     * The LoonieAllOfCredentials model constructor.
     * @property {module:model/LoonieAllOfCredentials}
     */
    LoonieAllOfCredentials,

    /**
     * The Manual model constructor.
     * @property {module:model/Manual}
     */
    Manual,

    /**
     * The Manual2 model constructor.
     * @property {module:model/Manual2}
     */
    Manual2,

    /**
     * The Manual2AllOfItems model constructor.
     * @property {module:model/Manual2AllOfItems}
     */
    Manual2AllOfItems,

    /**
     * The MiFinity model constructor.
     * @property {module:model/MiFinity}
     */
    MiFinity,

    /**
     * The MiFinityAllOfCredentials model constructor.
     * @property {module:model/MiFinityAllOfCredentials}
     */
    MiFinityAllOfCredentials,

    /**
     * The MinimumOrderAmount model constructor.
     * @property {module:model/MinimumOrderAmount}
     */
    MinimumOrderAmount,

    /**
     * The Moneris model constructor.
     * @property {module:model/Moneris}
     */
    Moneris,

    /**
     * The MonerisAllOfCredentials model constructor.
     * @property {module:model/MonerisAllOfCredentials}
     */
    MonerisAllOfCredentials,

    /**
     * The Money model constructor.
     * @property {module:model/Money}
     */
    Money,

    /**
     * The MtaPay model constructor.
     * @property {module:model/MtaPay}
     */
    MtaPay,

    /**
     * The MtaPayAllOfCredentials model constructor.
     * @property {module:model/MtaPayAllOfCredentials}
     */
    MtaPayAllOfCredentials,

    /**
     * The MtaPayAllOfSettings model constructor.
     * @property {module:model/MtaPayAllOfSettings}
     */
    MtaPayAllOfSettings,

    /**
     * The MuchBetter model constructor.
     * @property {module:model/MuchBetter}
     */
    MuchBetter,

    /**
     * The MuchBetterAllOfCredentials model constructor.
     * @property {module:model/MuchBetterAllOfCredentials}
     */
    MuchBetterAllOfCredentials,

    /**
     * The MuchBetterAllOfSettings model constructor.
     * @property {module:model/MuchBetterAllOfSettings}
     */
    MuchBetterAllOfSettings,

    /**
     * The MyFatoorah model constructor.
     * @property {module:model/MyFatoorah}
     */
    MyFatoorah,

    /**
     * The MyFatoorahAllOfCredentials model constructor.
     * @property {module:model/MyFatoorahAllOfCredentials}
     */
    MyFatoorahAllOfCredentials,

    /**
     * The NGenius model constructor.
     * @property {module:model/NGenius}
     */
    NGenius,

    /**
     * The NGenius3dsServer model constructor.
     * @property {module:model/NGenius3dsServer}
     */
    NGenius3dsServer,

    /**
     * The NGenius3dsServers model constructor.
     * @property {module:model/NGenius3dsServers}
     */
    NGenius3dsServers,

    /**
     * The NGeniusAllOfCredentials model constructor.
     * @property {module:model/NGeniusAllOfCredentials}
     */
    NGeniusAllOfCredentials,

    /**
     * The NMI model constructor.
     * @property {module:model/NMI}
     */
    NMI,

    /**
     * The NMI3dsServers model constructor.
     * @property {module:model/NMI3dsServers}
     */
    NMI3dsServers,

    /**
     * The NMIAllOfCredentials model constructor.
     * @property {module:model/NMIAllOfCredentials}
     */
    NMIAllOfCredentials,

    /**
     * The NMIAllOfSettings model constructor.
     * @property {module:model/NMIAllOfSettings}
     */
    NMIAllOfSettings,

    /**
     * The Neosurf model constructor.
     * @property {module:model/Neosurf}
     */
    Neosurf,

    /**
     * The NeosurfAllOfCredentials model constructor.
     * @property {module:model/NeosurfAllOfCredentials}
     */
    NeosurfAllOfCredentials,

    /**
     * The Netbanking model constructor.
     * @property {module:model/Netbanking}
     */
    Netbanking,

    /**
     * The NetbankingAllOfCredentials model constructor.
     * @property {module:model/NetbankingAllOfCredentials}
     */
    NetbankingAllOfCredentials,

    /**
     * The Neteller model constructor.
     * @property {module:model/Neteller}
     */
    Neteller,

    /**
     * The NetellerAllOfCredentials model constructor.
     * @property {module:model/NetellerAllOfCredentials}
     */
    NetellerAllOfCredentials,

    /**
     * The NetellerAllOfSettings model constructor.
     * @property {module:model/NetellerAllOfSettings}
     */
    NetellerAllOfSettings,

    /**
     * The NinjaWallet model constructor.
     * @property {module:model/NinjaWallet}
     */
    NinjaWallet,

    /**
     * The NinjaWalletAllOfCredentials model constructor.
     * @property {module:model/NinjaWalletAllOfCredentials}
     */
    NinjaWalletAllOfCredentials,

    /**
     * The NuaPay model constructor.
     * @property {module:model/NuaPay}
     */
    NuaPay,

    /**
     * The NuaPayAllOfCredentials model constructor.
     * @property {module:model/NuaPayAllOfCredentials}
     */
    NuaPayAllOfCredentials,

    /**
     * The OchaPay model constructor.
     * @property {module:model/OchaPay}
     */
    OchaPay,

    /**
     * The OchaPayAllOfCredentials model constructor.
     * @property {module:model/OchaPayAllOfCredentials}
     */
    OchaPayAllOfCredentials,

    /**
     * The OnBoardingUrlLink model constructor.
     * @property {module:model/OnBoardingUrlLink}
     */
    OnBoardingUrlLink,

    /**
     * The OnRamp model constructor.
     * @property {module:model/OnRamp}
     */
    OnRamp,

    /**
     * The OnRampAllOfCredentials model constructor.
     * @property {module:model/OnRampAllOfCredentials}
     */
    OnRampAllOfCredentials,

    /**
     * The OneColumn model constructor.
     * @property {module:model/OneColumn}
     */
    OneColumn,

    /**
     * The OneColumnAllOfData model constructor.
     * @property {module:model/OneColumnAllOfData}
     */
    OneColumnAllOfData,

    /**
     * The OneTimeOrder model constructor.
     * @property {module:model/OneTimeOrder}
     */
    OneTimeOrder,

    /**
     * The Onlineueberweisen model constructor.
     * @property {module:model/Onlineueberweisen}
     */
    Onlineueberweisen,

    /**
     * The OnlineueberweisenAllOfCredentials model constructor.
     * @property {module:model/OnlineueberweisenAllOfCredentials}
     */
    OnlineueberweisenAllOfCredentials,

    /**
     * The OnlineueberweisenAllOfSettings model constructor.
     * @property {module:model/OnlineueberweisenAllOfSettings}
     */
    OnlineueberweisenAllOfSettings,

    /**
     * The OrderTimeline model constructor.
     * @property {module:model/OrderTimeline}
     */
    OrderTimeline,

    /**
     * The Organization model constructor.
     * @property {module:model/Organization}
     */
    Organization,

    /**
     * The OrganizationEmbed model constructor.
     * @property {module:model/OrganizationEmbed}
     */
    OrganizationEmbed,

    /**
     * The OrganizationLink model constructor.
     * @property {module:model/OrganizationLink}
     */
    OrganizationLink,

    /**
     * The OrganizationQuestionnaire model constructor.
     * @property {module:model/OrganizationQuestionnaire}
     */
    OrganizationQuestionnaire,

    /**
     * The Other model constructor.
     * @property {module:model/Other}
     */
    Other,

    /**
     * The Paay3dsServer model constructor.
     * @property {module:model/Paay3dsServer}
     */
    Paay3dsServer,

    /**
     * The Pagsmile model constructor.
     * @property {module:model/Pagsmile}
     */
    Pagsmile,

    /**
     * The PagsmileAllOfCredentials model constructor.
     * @property {module:model/PagsmileAllOfCredentials}
     */
    PagsmileAllOfCredentials,

    /**
     * The PaidByTime model constructor.
     * @property {module:model/PaidByTime}
     */
    PaidByTime,

    /**
     * The Panamerican model constructor.
     * @property {module:model/Panamerican}
     */
    Panamerican,

    /**
     * The Panamerican3dsServer model constructor.
     * @property {module:model/Panamerican3dsServer}
     */
    Panamerican3dsServer,

    /**
     * The Panamerican3dsServers model constructor.
     * @property {module:model/Panamerican3dsServers}
     */
    Panamerican3dsServers,

    /**
     * The PanamericanAllOfCredentials model constructor.
     * @property {module:model/PanamericanAllOfCredentials}
     */
    PanamericanAllOfCredentials,

    /**
     * The PanamericanAllOfSettings model constructor.
     * @property {module:model/PanamericanAllOfSettings}
     */
    PanamericanAllOfSettings,

    /**
     * The PandaGateway model constructor.
     * @property {module:model/PandaGateway}
     */
    PandaGateway,

    /**
     * The PandaGatewayAllOfCredentials model constructor.
     * @property {module:model/PandaGatewayAllOfCredentials}
     */
    PandaGatewayAllOfCredentials,

    /**
     * The ParamountEft model constructor.
     * @property {module:model/ParamountEft}
     */
    ParamountEft,

    /**
     * The ParamountEftAllOfCredentials model constructor.
     * @property {module:model/ParamountEftAllOfCredentials}
     */
    ParamountEftAllOfCredentials,

    /**
     * The ParamountInterac model constructor.
     * @property {module:model/ParamountInterac}
     */
    ParamountInterac,

    /**
     * The ParamountInteracAllOfCredentials model constructor.
     * @property {module:model/ParamountInteracAllOfCredentials}
     */
    ParamountInteracAllOfCredentials,

    /**
     * The ParentTransactionEmbed model constructor.
     * @property {module:model/ParentTransactionEmbed}
     */
    ParentTransactionEmbed,

    /**
     * The ParentTransactionLink model constructor.
     * @property {module:model/ParentTransactionLink}
     */
    ParentTransactionLink,

    /**
     * The Partial model constructor.
     * @property {module:model/Partial}
     */
    Partial,

    /**
     * The Password model constructor.
     * @property {module:model/Password}
     */
    Password,

    /**
     * The Passwordless model constructor.
     * @property {module:model/Passwordless}
     */
    Passwordless,

    /**
     * The PatchKycRequestRequest model constructor.
     * @property {module:model/PatchKycRequestRequest}
     */
    PatchKycRequestRequest,

    /**
     * The PatchPaymentInstrumentRequest model constructor.
     * @property {module:model/PatchPaymentInstrumentRequest}
     */
    PatchPaymentInstrumentRequest,

    /**
     * The PatchTransactionRequest model constructor.
     * @property {module:model/PatchTransactionRequest}
     */
    PatchTransactionRequest,

    /**
     * The Pay4Fun model constructor.
     * @property {module:model/Pay4Fun}
     */
    Pay4Fun,

    /**
     * The Pay4FunAllOfCredentials model constructor.
     * @property {module:model/Pay4FunAllOfCredentials}
     */
    Pay4FunAllOfCredentials,

    /**
     * The PayCash model constructor.
     * @property {module:model/PayCash}
     */
    PayCash,

    /**
     * The PayCashAllOfCredentials model constructor.
     * @property {module:model/PayCashAllOfCredentials}
     */
    PayCashAllOfCredentials,

    /**
     * The PayClub model constructor.
     * @property {module:model/PayClub}
     */
    PayClub,

    /**
     * The PayClubAllOfCredentials model constructor.
     * @property {module:model/PayClubAllOfCredentials}
     */
    PayClubAllOfCredentials,

    /**
     * The PayClubAllOfSettings model constructor.
     * @property {module:model/PayClubAllOfSettings}
     */
    PayClubAllOfSettings,

    /**
     * The PayPal model constructor.
     * @property {module:model/PayPal}
     */
    PayPal,

    /**
     * The PayPalAccount model constructor.
     * @property {module:model/PayPalAccount}
     */
    PayPalAccount,

    /**
     * The PayPalAccountAllOfEmbedded model constructor.
     * @property {module:model/PayPalAccountAllOfEmbedded}
     */
    PayPalAccountAllOfEmbedded,

    /**
     * The PayPalAccountAllOfLinks model constructor.
     * @property {module:model/PayPalAccountAllOfLinks}
     */
    PayPalAccountAllOfLinks,

    /**
     * The PayPalAllOfSettings model constructor.
     * @property {module:model/PayPalAllOfSettings}
     */
    PayPalAllOfSettings,

    /**
     * The PayTabs model constructor.
     * @property {module:model/PayTabs}
     */
    PayTabs,

    /**
     * The PayTabsAllOfCredentials model constructor.
     * @property {module:model/PayTabsAllOfCredentials}
     */
    PayTabsAllOfCredentials,

    /**
     * The PayULatam model constructor.
     * @property {module:model/PayULatam}
     */
    PayULatam,

    /**
     * The PayULatamAllOfCredentials model constructor.
     * @property {module:model/PayULatamAllOfCredentials}
     */
    PayULatamAllOfCredentials,

    /**
     * The Payeezy model constructor.
     * @property {module:model/Payeezy}
     */
    Payeezy,

    /**
     * The PayeezyAllOfCredentials model constructor.
     * @property {module:model/PayeezyAllOfCredentials}
     */
    PayeezyAllOfCredentials,

    /**
     * The Payflow model constructor.
     * @property {module:model/Payflow}
     */
    Payflow,

    /**
     * The PayflowAllOfCredentials model constructor.
     * @property {module:model/PayflowAllOfCredentials}
     */
    PayflowAllOfCredentials,

    /**
     * The PaymenTechnologies model constructor.
     * @property {module:model/PaymenTechnologies}
     */
    PaymenTechnologies,

    /**
     * The PaymenTechnologiesAllOfCredentials model constructor.
     * @property {module:model/PaymenTechnologiesAllOfCredentials}
     */
    PaymenTechnologiesAllOfCredentials,

    /**
     * The PaymenTechnologiesAllOfSettings model constructor.
     * @property {module:model/PaymenTechnologiesAllOfSettings}
     */
    PaymenTechnologiesAllOfSettings,

    /**
     * The PaymentAsia model constructor.
     * @property {module:model/PaymentAsia}
     */
    PaymentAsia,

    /**
     * The PaymentAsiaAllOfCredentials model constructor.
     * @property {module:model/PaymentAsiaAllOfCredentials}
     */
    PaymentAsiaAllOfCredentials,

    /**
     * The PaymentCard model constructor.
     * @property {module:model/PaymentCard}
     */
    PaymentCard,

    /**
     * The PaymentCardAllOfEmbedded model constructor.
     * @property {module:model/PaymentCardAllOfEmbedded}
     */
    PaymentCardAllOfEmbedded,

    /**
     * The PaymentCardAllOfLinks model constructor.
     * @property {module:model/PaymentCardAllOfLinks}
     */
    PaymentCardAllOfLinks,

    /**
     * The PaymentCardBrand model constructor.
     * @property {module:model/PaymentCardBrand}
     */
    PaymentCardBrand,

    /**
     * The PaymentCardCreatePlain model constructor.
     * @property {module:model/PaymentCardCreatePlain}
     */
    PaymentCardCreatePlain,

    /**
     * The PaymentCardCreateToken model constructor.
     * @property {module:model/PaymentCardCreateToken}
     */
    PaymentCardCreateToken,

    /**
     * The PaymentCardDigitalWalletFeature model constructor.
     * @property {module:model/PaymentCardDigitalWalletFeature}
     */
    PaymentCardDigitalWalletFeature,

    /**
     * The PaymentCardEmbed model constructor.
     * @property {module:model/PaymentCardEmbed}
     */
    PaymentCardEmbed,

    /**
     * The PaymentCardLink model constructor.
     * @property {module:model/PaymentCardLink}
     */
    PaymentCardLink,

    /**
     * The PaymentCardToken model constructor.
     * @property {module:model/PaymentCardToken}
     */
    PaymentCardToken,

    /**
     * The PaymentCardUpdatePlain model constructor.
     * @property {module:model/PaymentCardUpdatePlain}
     */
    PaymentCardUpdatePlain,

    /**
     * The PaymentInstruction model constructor.
     * @property {module:model/PaymentInstruction}
     */
    PaymentInstruction,

    /**
     * The PaymentInstrument model constructor.
     * @property {module:model/PaymentInstrument}
     */
    PaymentInstrument,

    /**
     * The PaymentInstrument2 model constructor.
     * @property {module:model/PaymentInstrument2}
     */
    PaymentInstrument2,

    /**
     * The PaymentInstrument3 model constructor.
     * @property {module:model/PaymentInstrument3}
     */
    PaymentInstrument3,

    /**
     * The PaymentInstrumentCreateToken model constructor.
     * @property {module:model/PaymentInstrumentCreateToken}
     */
    PaymentInstrumentCreateToken,

    /**
     * The PaymentInstrumentUpdateToken model constructor.
     * @property {module:model/PaymentInstrumentUpdateToken}
     */
    PaymentInstrumentUpdateToken,

    /**
     * The PaymentMethod model constructor.
     * @property {module:model/PaymentMethod}
     */
    PaymentMethod,

    /**
     * The PaymentMethods model constructor.
     * @property {module:model/PaymentMethods}
     */
    PaymentMethods,

    /**
     * The PaymentRetry model constructor.
     * @property {module:model/PaymentRetry}
     */
    PaymentRetry,

    /**
     * The PaymentRetryAttemptsInner model constructor.
     * @property {module:model/PaymentRetryAttemptsInner}
     */
    PaymentRetryAttemptsInner,

    /**
     * The PaymentToken model constructor.
     * @property {module:model/PaymentToken}
     */
    PaymentToken,

    /**
     * The PaymentsOS model constructor.
     * @property {module:model/PaymentsOS}
     */
    PaymentsOS,

    /**
     * The PaymentsOSAllOfCredentials model constructor.
     * @property {module:model/PaymentsOSAllOfCredentials}
     */
    PaymentsOSAllOfCredentials,

    /**
     * The Paymero model constructor.
     * @property {module:model/Paymero}
     */
    Paymero,

    /**
     * The PaymeroAllOfCredentials model constructor.
     * @property {module:model/PaymeroAllOfCredentials}
     */
    PaymeroAllOfCredentials,

    /**
     * The PaymeroAllOfSettings model constructor.
     * @property {module:model/PaymeroAllOfSettings}
     */
    PaymeroAllOfSettings,

    /**
     * The PayoutRequest model constructor.
     * @property {module:model/PayoutRequest}
     */
    PayoutRequest,

    /**
     * The Payr model constructor.
     * @property {module:model/Payr}
     */
    Payr,

    /**
     * The PayrAllOfCredentials model constructor.
     * @property {module:model/PayrAllOfCredentials}
     */
    PayrAllOfCredentials,

    /**
     * The Paysafe model constructor.
     * @property {module:model/Paysafe}
     */
    Paysafe,

    /**
     * The Paysafe3dsServer model constructor.
     * @property {module:model/Paysafe3dsServer}
     */
    Paysafe3dsServer,

    /**
     * The Paysafe3dsServers model constructor.
     * @property {module:model/Paysafe3dsServers}
     */
    Paysafe3dsServers,

    /**
     * The PaysafeAllOfCredentials model constructor.
     * @property {module:model/PaysafeAllOfCredentials}
     */
    PaysafeAllOfCredentials,

    /**
     * The Paysafecash model constructor.
     * @property {module:model/Paysafecash}
     */
    Paysafecash,

    /**
     * The PaysafecashAllOfCredentials model constructor.
     * @property {module:model/PaysafecashAllOfCredentials}
     */
    PaysafecashAllOfCredentials,

    /**
     * The Payvision model constructor.
     * @property {module:model/Payvision}
     */
    Payvision,

    /**
     * The Payvision3dsServer model constructor.
     * @property {module:model/Payvision3dsServer}
     */
    Payvision3dsServer,

    /**
     * The Payvision3dsServers model constructor.
     * @property {module:model/Payvision3dsServers}
     */
    Payvision3dsServers,

    /**
     * The PayvisionAllOfCredentials model constructor.
     * @property {module:model/PayvisionAllOfCredentials}
     */
    PayvisionAllOfCredentials,

    /**
     * The PayvisionAllOfSettings model constructor.
     * @property {module:model/PayvisionAllOfSettings}
     */
    PayvisionAllOfSettings,

    /**
     * The Percent model constructor.
     * @property {module:model/Percent}
     */
    Percent,

    /**
     * The PermalinkLink model constructor.
     * @property {module:model/PermalinkLink}
     */
    PermalinkLink,

    /**
     * The Piastrix model constructor.
     * @property {module:model/Piastrix}
     */
    Piastrix,

    /**
     * The Piastrix3dsServer model constructor.
     * @property {module:model/Piastrix3dsServer}
     */
    Piastrix3dsServer,

    /**
     * The Piastrix3dsServers model constructor.
     * @property {module:model/Piastrix3dsServers}
     */
    Piastrix3dsServers,

    /**
     * The PiastrixAllOfCredentials model constructor.
     * @property {module:model/PiastrixAllOfCredentials}
     */
    PiastrixAllOfCredentials,

    /**
     * The PiastrixAllOfSettings model constructor.
     * @property {module:model/PiastrixAllOfSettings}
     */
    PiastrixAllOfSettings,

    /**
     * The PlaidAccountToken model constructor.
     * @property {module:model/PlaidAccountToken}
     */
    PlaidAccountToken,

    /**
     * The Plan model constructor.
     * @property {module:model/Plan}
     */
    Plan,

    /**
     * The PlanBillingTiming model constructor.
     * @property {module:model/PlanBillingTiming}
     */
    PlanBillingTiming,

    /**
     * The PlanEmbed model constructor.
     * @property {module:model/PlanEmbed}
     */
    PlanEmbed,

    /**
     * The PlanPeriod model constructor.
     * @property {module:model/PlanPeriod}
     */
    PlanPeriod,

    /**
     * The PlanPriceFormula model constructor.
     * @property {module:model/PlanPriceFormula}
     */
    PlanPriceFormula,

    /**
     * The Plugnpay model constructor.
     * @property {module:model/Plugnpay}
     */
    Plugnpay,

    /**
     * The PlugnpayAllOfCredentials model constructor.
     * @property {module:model/PlugnpayAllOfCredentials}
     */
    PlugnpayAllOfCredentials,

    /**
     * The PostBankAccountRequest model constructor.
     * @property {module:model/PostBankAccountRequest}
     */
    PostBankAccountRequest,

    /**
     * The PostFileRequest model constructor.
     * @property {module:model/PostFileRequest}
     */
    PostFileRequest,

    /**
     * The PostFinance model constructor.
     * @property {module:model/PostFinance}
     */
    PostFinance,

    /**
     * The PostFinanceAllOfCredentials model constructor.
     * @property {module:model/PostFinanceAllOfCredentials}
     */
    PostFinanceAllOfCredentials,

    /**
     * The PostKycDocumentMatchesRequest model constructor.
     * @property {module:model/PostKycDocumentMatchesRequest}
     */
    PostKycDocumentMatchesRequest,

    /**
     * The PostPaymentCardRequest model constructor.
     * @property {module:model/PostPaymentCardRequest}
     */
    PostPaymentCardRequest,

    /**
     * The PostPaymentInstrumentRequest model constructor.
     * @property {module:model/PostPaymentInstrumentRequest}
     */
    PostPaymentInstrumentRequest,

    /**
     * The PostTagCustomerCollectionRequest model constructor.
     * @property {module:model/PostTagCustomerCollectionRequest}
     */
    PostTagCustomerCollectionRequest,

    /**
     * The PriceBasedShippingRate model constructor.
     * @property {module:model/PriceBasedShippingRate}
     */
    PriceBasedShippingRate,

    /**
     * The Problem model constructor.
     * @property {module:model/Problem}
     */
    Problem,

    /**
     * The Product model constructor.
     * @property {module:model/Product}
     */
    Product,

    /**
     * The ProductEmbed model constructor.
     * @property {module:model/ProductEmbed}
     */
    ProductEmbed,

    /**
     * The ProductLink model constructor.
     * @property {module:model/ProductLink}
     */
    ProductLink,

    /**
     * The ProofOfAddress model constructor.
     * @property {module:model/ProofOfAddress}
     */
    ProofOfAddress,

    /**
     * The ProofOfAddressAllOfDocumentMatches model constructor.
     * @property {module:model/ProofOfAddressAllOfDocumentMatches}
     */
    ProofOfAddressAllOfDocumentMatches,

    /**
     * The ProofOfAddressAllOfLinks model constructor.
     * @property {module:model/ProofOfAddressAllOfLinks}
     */
    ProofOfAddressAllOfLinks,

    /**
     * The ProofOfFunds model constructor.
     * @property {module:model/ProofOfFunds}
     */
    ProofOfFunds,

    /**
     * The ProofOfIdentity model constructor.
     * @property {module:model/ProofOfIdentity}
     */
    ProofOfIdentity,

    /**
     * The ProofOfIdentityAllOfDocumentMatches model constructor.
     * @property {module:model/ProofOfIdentityAllOfDocumentMatches}
     */
    ProofOfIdentityAllOfDocumentMatches,

    /**
     * The ProofOfIdentityAllOfLinks model constructor.
     * @property {module:model/ProofOfIdentityAllOfLinks}
     */
    ProofOfIdentityAllOfLinks,

    /**
     * The ProofOfPurchase model constructor.
     * @property {module:model/ProofOfPurchase}
     */
    ProofOfPurchase,

    /**
     * The Prosa model constructor.
     * @property {module:model/Prosa}
     */
    Prosa,

    /**
     * The ProsaAllOfCredentials model constructor.
     * @property {module:model/ProsaAllOfCredentials}
     */
    ProsaAllOfCredentials,

    /**
     * The PurchaseBumpOffer model constructor.
     * @property {module:model/PurchaseBumpOffer}
     */
    PurchaseBumpOffer,

    /**
     * The PurchaseBumpStatus model constructor.
     * @property {module:model/PurchaseBumpStatus}
     */
    PurchaseBumpStatus,

    /**
     * The QueryUrlLink model constructor.
     * @property {module:model/QueryUrlLink}
     */
    QueryUrlLink,

    /**
     * The RPN model constructor.
     * @property {module:model/RPN}
     */
    RPN,

    /**
     * The RPNAllOfCredentials model constructor.
     * @property {module:model/RPNAllOfCredentials}
     */
    RPNAllOfCredentials,

    /**
     * The Rapyd model constructor.
     * @property {module:model/Rapyd}
     */
    Rapyd,

    /**
     * The RapydAllOfCredentials model constructor.
     * @property {module:model/RapydAllOfCredentials}
     */
    RapydAllOfCredentials,

    /**
     * The ReadyToPay model constructor.
     * @property {module:model/ReadyToPay}
     */
    ReadyToPay,

    /**
     * The ReadyToPayAchMethod model constructor.
     * @property {module:model/ReadyToPayAchMethod}
     */
    ReadyToPayAchMethod,

    /**
     * The ReadyToPayAchMethodFeature model constructor.
     * @property {module:model/ReadyToPayAchMethodFeature}
     */
    ReadyToPayAchMethodFeature,

    /**
     * The ReadyToPayAmount model constructor.
     * @property {module:model/ReadyToPayAmount}
     */
    ReadyToPayAmount,

    /**
     * The ReadyToPayGenericMethod model constructor.
     * @property {module:model/ReadyToPayGenericMethod}
     */
    ReadyToPayGenericMethod,

    /**
     * The ReadyToPayItems model constructor.
     * @property {module:model/ReadyToPayItems}
     */
    ReadyToPayItems,

    /**
     * The ReadyToPayItemsItemsInner model constructor.
     * @property {module:model/ReadyToPayItemsItemsInner}
     */
    ReadyToPayItemsItemsInner,

    /**
     * The ReadyToPayMethodsInner model constructor.
     * @property {module:model/ReadyToPayMethodsInner}
     */
    ReadyToPayMethodsInner,

    /**
     * The ReadyToPayPaymentCardMethod model constructor.
     * @property {module:model/ReadyToPayPaymentCardMethod}
     */
    ReadyToPayPaymentCardMethod,

    /**
     * The ReadyToPayPaymentCardMethodFeature model constructor.
     * @property {module:model/ReadyToPayPaymentCardMethodFeature}
     */
    ReadyToPayPaymentCardMethodFeature,

    /**
     * The Realex model constructor.
     * @property {module:model/Realex}
     */
    Realex,

    /**
     * The RealexAllOfCredentials model constructor.
     * @property {module:model/RealexAllOfCredentials}
     */
    RealexAllOfCredentials,

    /**
     * The Realtime model constructor.
     * @property {module:model/Realtime}
     */
    Realtime,

    /**
     * The RealtimeAllOfCredentials model constructor.
     * @property {module:model/RealtimeAllOfCredentials}
     */
    RealtimeAllOfCredentials,

    /**
     * The Rebilly model constructor.
     * @property {module:model/Rebilly}
     */
    Rebilly,

    /**
     * The RebillyTaxjar model constructor.
     * @property {module:model/RebillyTaxjar}
     */
    RebillyTaxjar,

    /**
     * The RebillyTaxjarAllOfItems model constructor.
     * @property {module:model/RebillyTaxjarAllOfItems}
     */
    RebillyTaxjarAllOfItems,

    /**
     * The RecalculateInvoiceLink model constructor.
     * @property {module:model/RecalculateInvoiceLink}
     */
    RecalculateInvoiceLink,

    /**
     * The RecentInvoiceEmbed model constructor.
     * @property {module:model/RecentInvoiceEmbed}
     */
    RecentInvoiceEmbed,

    /**
     * The RecentInvoiceLink model constructor.
     * @property {module:model/RecentInvoiceLink}
     */
    RecentInvoiceLink,

    /**
     * The RedemptionCancel model constructor.
     * @property {module:model/RedemptionCancel}
     */
    RedemptionCancel,

    /**
     * The RedemptionRestriction model constructor.
     * @property {module:model/RedemptionRestriction}
     */
    RedemptionRestriction,

    /**
     * The RedemptionsPerCustomer model constructor.
     * @property {module:model/RedemptionsPerCustomer}
     */
    RedemptionsPerCustomer,

    /**
     * The Redsys model constructor.
     * @property {module:model/Redsys}
     */
    Redsys,

    /**
     * The RedsysAllOfCredentials model constructor.
     * @property {module:model/RedsysAllOfCredentials}
     */
    RedsysAllOfCredentials,

    /**
     * The RefundUrlLink model constructor.
     * @property {module:model/RefundUrlLink}
     */
    RefundUrlLink,

    /**
     * The ResendEmail model constructor.
     * @property {module:model/ResendEmail}
     */
    ResendEmail,

    /**
     * The ResetPasswordToken model constructor.
     * @property {module:model/ResetPasswordToken}
     */
    ResetPasswordToken,

    /**
     * The RestrictToInvoices model constructor.
     * @property {module:model/RestrictToInvoices}
     */
    RestrictToInvoices,

    /**
     * The RestrictToPlans model constructor.
     * @property {module:model/RestrictToPlans}
     */
    RestrictToPlans,

    /**
     * The RestrictToProducts model constructor.
     * @property {module:model/RestrictToProducts}
     */
    RestrictToProducts,

    /**
     * The RestrictToSubscriptions model constructor.
     * @property {module:model/RestrictToSubscriptions}
     */
    RestrictToSubscriptions,

    /**
     * The RetriedTransactionEmbed model constructor.
     * @property {module:model/RetriedTransactionEmbed}
     */
    RetriedTransactionEmbed,

    /**
     * The RetriedTransactionLink model constructor.
     * @property {module:model/RetriedTransactionLink}
     */
    RetriedTransactionLink,

    /**
     * The RiskMetadata model constructor.
     * @property {module:model/RiskMetadata}
     */
    RiskMetadata,

    /**
     * The Rotessa model constructor.
     * @property {module:model/Rotessa}
     */
    Rotessa,

    /**
     * The RotessaAllOfCredentials model constructor.
     * @property {module:model/RotessaAllOfCredentials}
     */
    RotessaAllOfCredentials,

    /**
     * The RotessaAllOfSettings model constructor.
     * @property {module:model/RotessaAllOfSettings}
     */
    RotessaAllOfSettings,

    /**
     * The RulesetRestore model constructor.
     * @property {module:model/RulesetRestore}
     */
    RulesetRestore,

    /**
     * The SMSVoucher model constructor.
     * @property {module:model/SMSVoucher}
     */
    SMSVoucher,

    /**
     * The SMSVoucherAllOfCredentials model constructor.
     * @property {module:model/SMSVoucherAllOfCredentials}
     */
    SMSVoucherAllOfCredentials,

    /**
     * The Sagepay model constructor.
     * @property {module:model/Sagepay}
     */
    Sagepay,

    /**
     * The SagepayAllOfCredentials model constructor.
     * @property {module:model/SagepayAllOfCredentials}
     */
    SagepayAllOfCredentials,

    /**
     * The SaltarPay model constructor.
     * @property {module:model/SaltarPay}
     */
    SaltarPay,

    /**
     * The SaltarPayAllOfCredentials model constructor.
     * @property {module:model/SaltarPayAllOfCredentials}
     */
    SaltarPayAllOfCredentials,

    /**
     * The SeamlessChex model constructor.
     * @property {module:model/SeamlessChex}
     */
    SeamlessChex,

    /**
     * The SeamlessChexAllOfCredentials model constructor.
     * @property {module:model/SeamlessChexAllOfCredentials}
     */
    SeamlessChexAllOfCredentials,

    /**
     * The Search model constructor.
     * @property {module:model/Search}
     */
    Search,

    /**
     * The SecureTrading model constructor.
     * @property {module:model/SecureTrading}
     */
    SecureTrading,

    /**
     * The SecureTrading3dsServer model constructor.
     * @property {module:model/SecureTrading3dsServer}
     */
    SecureTrading3dsServer,

    /**
     * The SecureTrading3dsServers model constructor.
     * @property {module:model/SecureTrading3dsServers}
     */
    SecureTrading3dsServers,

    /**
     * The SecureTradingAllOfCredentials model constructor.
     * @property {module:model/SecureTradingAllOfCredentials}
     */
    SecureTradingAllOfCredentials,

    /**
     * The SecurionPay model constructor.
     * @property {module:model/SecurionPay}
     */
    SecurionPay,

    /**
     * The SecurionPay3dsServers model constructor.
     * @property {module:model/SecurionPay3dsServers}
     */
    SecurionPay3dsServers,

    /**
     * The SecurionPayAllOfCredentials model constructor.
     * @property {module:model/SecurionPayAllOfCredentials}
     */
    SecurionPayAllOfCredentials,

    /**
     * The SelfLink model constructor.
     * @property {module:model/SelfLink}
     */
    SelfLink,

    /**
     * The ServicePeriodAnchorInstruction model constructor.
     * @property {module:model/ServicePeriodAnchorInstruction}
     */
    ServicePeriodAnchorInstruction,

    /**
     * The ShippingZone model constructor.
     * @property {module:model/ShippingZone}
     */
    ShippingZone,

    /**
     * The SignedLinkLink model constructor.
     * @property {module:model/SignedLinkLink}
     */
    SignedLinkLink,

    /**
     * The Skrill model constructor.
     * @property {module:model/Skrill}
     */
    Skrill,

    /**
     * The SkrillAllOfCredentials model constructor.
     * @property {module:model/SkrillAllOfCredentials}
     */
    SkrillAllOfCredentials,

    /**
     * The SmartInvoice model constructor.
     * @property {module:model/SmartInvoice}
     */
    SmartInvoice,

    /**
     * The SmartInvoice3dsServer model constructor.
     * @property {module:model/SmartInvoice3dsServer}
     */
    SmartInvoice3dsServer,

    /**
     * The SmartInvoice3dsServers model constructor.
     * @property {module:model/SmartInvoice3dsServers}
     */
    SmartInvoice3dsServers,

    /**
     * The SmartInvoiceAllOfCredentials model constructor.
     * @property {module:model/SmartInvoiceAllOfCredentials}
     */
    SmartInvoiceAllOfCredentials,

    /**
     * The Sofort model constructor.
     * @property {module:model/Sofort}
     */
    Sofort,

    /**
     * The SofortAllOfCredentials model constructor.
     * @property {module:model/SofortAllOfCredentials}
     */
    SofortAllOfCredentials,

    /**
     * The SparkPay model constructor.
     * @property {module:model/SparkPay}
     */
    SparkPay,

    /**
     * The SparkPayAllOfCredentials model constructor.
     * @property {module:model/SparkPayAllOfCredentials}
     */
    SparkPayAllOfCredentials,

    /**
     * The Stairstep model constructor.
     * @property {module:model/Stairstep}
     */
    Stairstep,

    /**
     * The StairstepAllOfBrackets model constructor.
     * @property {module:model/StairstepAllOfBrackets}
     */
    StairstepAllOfBrackets,

    /**
     * The StaticGateway model constructor.
     * @property {module:model/StaticGateway}
     */
    StaticGateway,

    /**
     * The StaticIpnLink model constructor.
     * @property {module:model/StaticIpnLink}
     */
    StaticIpnLink,

    /**
     * The Stripe model constructor.
     * @property {module:model/Stripe}
     */
    Stripe,

    /**
     * The Stripe3dsServer model constructor.
     * @property {module:model/Stripe3dsServer}
     */
    Stripe3dsServer,

    /**
     * The Stripe3dsServers model constructor.
     * @property {module:model/Stripe3dsServers}
     */
    Stripe3dsServers,

    /**
     * The StripeAllOfSettings model constructor.
     * @property {module:model/StripeAllOfSettings}
     */
    StripeAllOfSettings,

    /**
     * The Subscription model constructor.
     * @property {module:model/Subscription}
     */
    Subscription,

    /**
     * The SubscriptionCancellation model constructor.
     * @property {module:model/SubscriptionCancellation}
     */
    SubscriptionCancellation,

    /**
     * The SubscriptionCancellationState model constructor.
     * @property {module:model/SubscriptionCancellationState}
     */
    SubscriptionCancellationState,

    /**
     * The SubscriptionChange model constructor.
     * @property {module:model/SubscriptionChange}
     */
    SubscriptionChange,

    /**
     * The SubscriptionChangeItemsInner model constructor.
     * @property {module:model/SubscriptionChangeItemsInner}
     */
    SubscriptionChangeItemsInner,

    /**
     * The SubscriptionInvoice model constructor.
     * @property {module:model/SubscriptionInvoice}
     */
    SubscriptionInvoice,

    /**
     * The SubscriptionLink model constructor.
     * @property {module:model/SubscriptionLink}
     */
    SubscriptionLink,

    /**
     * The SubscriptionMetadata model constructor.
     * @property {module:model/SubscriptionMetadata}
     */
    SubscriptionMetadata,

    /**
     * The SubscriptionMetadataEmbeddedInner model constructor.
     * @property {module:model/SubscriptionMetadataEmbeddedInner}
     */
    SubscriptionMetadataEmbeddedInner,

    /**
     * The SubscriptionMetadataLinksInner model constructor.
     * @property {module:model/SubscriptionMetadataLinksInner}
     */
    SubscriptionMetadataLinksInner,

    /**
     * The SubscriptionOrder model constructor.
     * @property {module:model/SubscriptionOrder}
     */
    SubscriptionOrder,

    /**
     * The SubscriptionReactivation model constructor.
     * @property {module:model/SubscriptionReactivation}
     */
    SubscriptionReactivation,

    /**
     * The TWINT model constructor.
     * @property {module:model/TWINT}
     */
    TWINT,

    /**
     * The TWINTAllOfCredentials model constructor.
     * @property {module:model/TWINTAllOfCredentials}
     */
    TWINTAllOfCredentials,

    /**
     * The TWINTAllOfSettings model constructor.
     * @property {module:model/TWINTAllOfSettings}
     */
    TWINTAllOfSettings,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The TestProcessor model constructor.
     * @property {module:model/TestProcessor}
     */
    TestProcessor,

    /**
     * The TestProcessor3dsServer model constructor.
     * @property {module:model/TestProcessor3dsServer}
     */
    TestProcessor3dsServer,

    /**
     * The TestProcessor3dsServers model constructor.
     * @property {module:model/TestProcessor3dsServers}
     */
    TestProcessor3dsServers,

    /**
     * The ThreeColumns model constructor.
     * @property {module:model/ThreeColumns}
     */
    ThreeColumns,

    /**
     * The ThreeColumnsAllOfData model constructor.
     * @property {module:model/ThreeColumnsAllOfData}
     */
    ThreeColumnsAllOfData,

    /**
     * The ThreeDSecure model constructor.
     * @property {module:model/ThreeDSecure}
     */
    ThreeDSecure,

    /**
     * The ThreeDSecureIO3dsServer model constructor.
     * @property {module:model/ThreeDSecureIO3dsServer}
     */
    ThreeDSecureIO3dsServer,

    /**
     * The ThreeDSecureResult model constructor.
     * @property {module:model/ThreeDSecureResult}
     */
    ThreeDSecureResult,

    /**
     * The ThreeDSecureServerName model constructor.
     * @property {module:model/ThreeDSecureServerName}
     */
    ThreeDSecureServerName,

    /**
     * The Tiered model constructor.
     * @property {module:model/Tiered}
     */
    Tiered,

    /**
     * The TimePluralUnit model constructor.
     * @property {module:model/TimePluralUnit}
     */
    TimePluralUnit,

    /**
     * The TimeUnit model constructor.
     * @property {module:model/TimeUnit}
     */
    TimeUnit,

    /**
     * The TimelineAction model constructor.
     * @property {module:model/TimelineAction}
     */
    TimelineAction,

    /**
     * The TimelineExtraData model constructor.
     * @property {module:model/TimelineExtraData}
     */
    TimelineExtraData,

    /**
     * The TimelineExtraDataAuthor model constructor.
     * @property {module:model/TimelineExtraDataAuthor}
     */
    TimelineExtraDataAuthor,

    /**
     * The TimelineExtraDataLinksInner model constructor.
     * @property {module:model/TimelineExtraDataLinksInner}
     */
    TimelineExtraDataLinksInner,

    /**
     * The TimelineTable model constructor.
     * @property {module:model/TimelineTable}
     */
    TimelineTable,

    /**
     * The ToditoCash model constructor.
     * @property {module:model/ToditoCash}
     */
    ToditoCash,

    /**
     * The ToditoCashAllOfCredentials model constructor.
     * @property {module:model/ToditoCashAllOfCredentials}
     */
    ToditoCashAllOfCredentials,

    /**
     * The TotalRedemptions model constructor.
     * @property {module:model/TotalRedemptions}
     */
    TotalRedemptions,

    /**
     * The Transaction model constructor.
     * @property {module:model/Transaction}
     */
    Transaction,

    /**
     * The TransactionAllOfBumpOffer model constructor.
     * @property {module:model/TransactionAllOfBumpOffer}
     */
    TransactionAllOfBumpOffer,

    /**
     * The TransactionAllOfDcc model constructor.
     * @property {module:model/TransactionAllOfDcc}
     */
    TransactionAllOfDcc,

    /**
     * The TransactionAllOfEmbedded model constructor.
     * @property {module:model/TransactionAllOfEmbedded}
     */
    TransactionAllOfEmbedded,

    /**
     * The TransactionAllOfGateway model constructor.
     * @property {module:model/TransactionAllOfGateway}
     */
    TransactionAllOfGateway,

    /**
     * The TransactionAllOfGatewayAvsResponse model constructor.
     * @property {module:model/TransactionAllOfGatewayAvsResponse}
     */
    TransactionAllOfGatewayAvsResponse,

    /**
     * The TransactionAllOfGatewayCvvResponse model constructor.
     * @property {module:model/TransactionAllOfGatewayCvvResponse}
     */
    TransactionAllOfGatewayCvvResponse,

    /**
     * The TransactionAllOfGatewayResponse model constructor.
     * @property {module:model/TransactionAllOfGatewayResponse}
     */
    TransactionAllOfGatewayResponse,

    /**
     * The TransactionAllOfLinks model constructor.
     * @property {module:model/TransactionAllOfLinks}
     */
    TransactionAllOfLinks,

    /**
     * The TransactionAllocationsLink model constructor.
     * @property {module:model/TransactionAllocationsLink}
     */
    TransactionAllocationsLink,

    /**
     * The TransactionEmbed model constructor.
     * @property {module:model/TransactionEmbed}
     */
    TransactionEmbed,

    /**
     * The TransactionLink model constructor.
     * @property {module:model/TransactionLink}
     */
    TransactionLink,

    /**
     * The TransactionQuery model constructor.
     * @property {module:model/TransactionQuery}
     */
    TransactionQuery,

    /**
     * The TransactionRefund model constructor.
     * @property {module:model/TransactionRefund}
     */
    TransactionRefund,

    /**
     * The TransactionRequest model constructor.
     * @property {module:model/TransactionRequest}
     */
    TransactionRequest,

    /**
     * The TransactionTimeline model constructor.
     * @property {module:model/TransactionTimeline}
     */
    TransactionTimeline,

    /**
     * The TransactionUpdate model constructor.
     * @property {module:model/TransactionUpdate}
     */
    TransactionUpdate,

    /**
     * The TransactionUpdateUrlLink model constructor.
     * @property {module:model/TransactionUpdateUrlLink}
     */
    TransactionUpdateUrlLink,

    /**
     * The TrustPay model constructor.
     * @property {module:model/TrustPay}
     */
    TrustPay,

    /**
     * The TrustPayAllOfCredentials model constructor.
     * @property {module:model/TrustPayAllOfCredentials}
     */
    TrustPayAllOfCredentials,

    /**
     * The Trustly model constructor.
     * @property {module:model/Trustly}
     */
    Trustly,

    /**
     * The TrustlyAllOfCredentials model constructor.
     * @property {module:model/TrustlyAllOfCredentials}
     */
    TrustlyAllOfCredentials,

    /**
     * The TrustsPay model constructor.
     * @property {module:model/TrustsPay}
     */
    TrustsPay,

    /**
     * The TrustsPayAllOfCredentials model constructor.
     * @property {module:model/TrustsPayAllOfCredentials}
     */
    TrustsPayAllOfCredentials,

    /**
     * The TwoColumns model constructor.
     * @property {module:model/TwoColumns}
     */
    TwoColumns,

    /**
     * The UPayCard model constructor.
     * @property {module:model/UPayCard}
     */
    UPayCard,

    /**
     * The UPayCardAllOfCredentials model constructor.
     * @property {module:model/UPayCardAllOfCredentials}
     */
    UPayCardAllOfCredentials,

    /**
     * The UPayCardAllOfSettings model constructor.
     * @property {module:model/UPayCardAllOfSettings}
     */
    UPayCardAllOfSettings,

    /**
     * The USAePay model constructor.
     * @property {module:model/USAePay}
     */
    USAePay,

    /**
     * The USAePayAllOfCredentials model constructor.
     * @property {module:model/USAePayAllOfCredentials}
     */
    USAePayAllOfCredentials,

    /**
     * The UpcomingInvoiceItem model constructor.
     * @property {module:model/UpcomingInvoiceItem}
     */
    UpcomingInvoiceItem,

    /**
     * The VCreditos model constructor.
     * @property {module:model/VCreditos}
     */
    VCreditos,

    /**
     * The VCreditosAllOfCredentials model constructor.
     * @property {module:model/VCreditosAllOfCredentials}
     */
    VCreditosAllOfCredentials,

    /**
     * The ValidationErrorExtensions model constructor.
     * @property {module:model/ValidationErrorExtensions}
     */
    ValidationErrorExtensions,

    /**
     * The ValidationErrorExtensionsInvalidFieldsInner model constructor.
     * @property {module:model/ValidationErrorExtensionsInvalidFieldsInner}
     */
    ValidationErrorExtensionsInvalidFieldsInner,

    /**
     * The VantivLitle model constructor.
     * @property {module:model/VantivLitle}
     */
    VantivLitle,

    /**
     * The VantivLitle3dsServers model constructor.
     * @property {module:model/VantivLitle3dsServers}
     */
    VantivLitle3dsServers,

    /**
     * The VantivLitleAllOfCredentials model constructor.
     * @property {module:model/VantivLitleAllOfCredentials}
     */
    VantivLitleAllOfCredentials,

    /**
     * The VaultedInstrument model constructor.
     * @property {module:model/VaultedInstrument}
     */
    VaultedInstrument,

    /**
     * The VegaaH model constructor.
     * @property {module:model/VegaaH}
     */
    VegaaH,

    /**
     * The VegaaHAllOfCredentials model constructor.
     * @property {module:model/VegaaHAllOfCredentials}
     */
    VegaaHAllOfCredentials,

    /**
     * The Volume model constructor.
     * @property {module:model/Volume}
     */
    Volume,

    /**
     * The Wallet88 model constructor.
     * @property {module:model/Wallet88}
     */
    Wallet88,

    /**
     * The Wallet88AllOfCredentials model constructor.
     * @property {module:model/Wallet88AllOfCredentials}
     */
    Wallet88AllOfCredentials,

    /**
     * The Walpay model constructor.
     * @property {module:model/Walpay}
     */
    Walpay,

    /**
     * The Walpay3dsServers model constructor.
     * @property {module:model/Walpay3dsServers}
     */
    Walpay3dsServers,

    /**
     * The WalpayAllOfCredentials model constructor.
     * @property {module:model/WalpayAllOfCredentials}
     */
    WalpayAllOfCredentials,

    /**
     * The WebsiteEmbed model constructor.
     * @property {module:model/WebsiteEmbed}
     */
    WebsiteEmbed,

    /**
     * The WebsiteLink model constructor.
     * @property {module:model/WebsiteLink}
     */
    WebsiteLink,

    /**
     * The Wirecard model constructor.
     * @property {module:model/Wirecard}
     */
    Wirecard,

    /**
     * The Wirecard3dsServer model constructor.
     * @property {module:model/Wirecard3dsServer}
     */
    Wirecard3dsServer,

    /**
     * The Wirecard3dsServers model constructor.
     * @property {module:model/Wirecard3dsServers}
     */
    Wirecard3dsServers,

    /**
     * The WirecardAllOfCredentials model constructor.
     * @property {module:model/WirecardAllOfCredentials}
     */
    WirecardAllOfCredentials,

    /**
     * The WorldlineAtosFrankfurt model constructor.
     * @property {module:model/WorldlineAtosFrankfurt}
     */
    WorldlineAtosFrankfurt,

    /**
     * The WorldlineAtosFrankfurt3dsServers model constructor.
     * @property {module:model/WorldlineAtosFrankfurt3dsServers}
     */
    WorldlineAtosFrankfurt3dsServers,

    /**
     * The WorldlineAtosFrankfurtAllOfCredentials model constructor.
     * @property {module:model/WorldlineAtosFrankfurtAllOfCredentials}
     */
    WorldlineAtosFrankfurtAllOfCredentials,

    /**
     * The WorldlineAtosFrankfurtAllOfSettings model constructor.
     * @property {module:model/WorldlineAtosFrankfurtAllOfSettings}
     */
    WorldlineAtosFrankfurtAllOfSettings,

    /**
     * The Worldpay model constructor.
     * @property {module:model/Worldpay}
     */
    Worldpay,

    /**
     * The Worldpay3dsServers model constructor.
     * @property {module:model/Worldpay3dsServers}
     */
    Worldpay3dsServers,

    /**
     * The WorldpayAllOfCredentials model constructor.
     * @property {module:model/WorldpayAllOfCredentials}
     */
    WorldpayAllOfCredentials,

    /**
     * The WorldpayAllOfSettings model constructor.
     * @property {module:model/WorldpayAllOfSettings}
     */
    WorldpayAllOfSettings,

    /**
     * The XPay model constructor.
     * @property {module:model/XPay}
     */
    XPay,

    /**
     * The XPayAllOfCredentials model constructor.
     * @property {module:model/XPayAllOfCredentials}
     */
    XPayAllOfCredentials,

    /**
     * The Zimpler model constructor.
     * @property {module:model/Zimpler}
     */
    Zimpler,

    /**
     * The ZimplerAllOfCredentials model constructor.
     * @property {module:model/ZimplerAllOfCredentials}
     */
    ZimplerAllOfCredentials,

    /**
     * The Zotapay model constructor.
     * @property {module:model/Zotapay}
     */
    Zotapay,

    /**
     * The ZotapayAllOfCredentials model constructor.
     * @property {module:model/ZotapayAllOfCredentials}
     */
    ZotapayAllOfCredentials,

    /**
    * The AMLApi service constructor.
    * @property {module:api/AMLApi}
    */
    AMLApi,

    /**
    * The BankAccountsApi service constructor.
    * @property {module:api/BankAccountsApi}
    */
    BankAccountsApi,

    /**
    * The BlocklistsApi service constructor.
    * @property {module:api/BlocklistsApi}
    */
    BlocklistsApi,

    /**
    * The Class3DSecureApi service constructor.
    * @property {module:api/Class3DSecureApi}
    */
    Class3DSecureApi,

    /**
    * The CouponsApi service constructor.
    * @property {module:api/CouponsApi}
    */
    CouponsApi,

    /**
    * The CustomFieldsApi service constructor.
    * @property {module:api/CustomFieldsApi}
    */
    CustomFieldsApi,

    /**
    * The CustomerAuthenticationApi service constructor.
    * @property {module:api/CustomerAuthenticationApi}
    */
    CustomerAuthenticationApi,

    /**
    * The CustomersApi service constructor.
    * @property {module:api/CustomersApi}
    */
    CustomersApi,

    /**
    * The CustomersTimelineApi service constructor.
    * @property {module:api/CustomersTimelineApi}
    */
    CustomersTimelineApi,

    /**
    * The DisputesApi service constructor.
    * @property {module:api/DisputesApi}
    */
    DisputesApi,

    /**
    * The FilesApi service constructor.
    * @property {module:api/FilesApi}
    */
    FilesApi,

    /**
    * The InvoicesApi service constructor.
    * @property {module:api/InvoicesApi}
    */
    InvoicesApi,

    /**
    * The KYCDocumentsApi service constructor.
    * @property {module:api/KYCDocumentsApi}
    */
    KYCDocumentsApi,

    /**
    * The OrdersApi service constructor.
    * @property {module:api/OrdersApi}
    */
    OrdersApi,

    /**
    * The PayPalAccountsApi service constructor.
    * @property {module:api/PayPalAccountsApi}
    */
    PayPalAccountsApi,

    /**
    * The PaymentCardsApi service constructor.
    * @property {module:api/PaymentCardsApi}
    */
    PaymentCardsApi,

    /**
    * The PaymentInstrumentsApi service constructor.
    * @property {module:api/PaymentInstrumentsApi}
    */
    PaymentInstrumentsApi,

    /**
    * The PaymentTokensApi service constructor.
    * @property {module:api/PaymentTokensApi}
    */
    PaymentTokensApi,

    /**
    * The PlansApi service constructor.
    * @property {module:api/PlansApi}
    */
    PlansApi,

    /**
    * The ProductsApi service constructor.
    * @property {module:api/ProductsApi}
    */
    ProductsApi,

    /**
    * The SearchApi service constructor.
    * @property {module:api/SearchApi}
    */
    SearchApi,

    /**
    * The ShippingZonesApi service constructor.
    * @property {module:api/ShippingZonesApi}
    */
    ShippingZonesApi,

    /**
    * The TagsApi service constructor.
    * @property {module:api/TagsApi}
    */
    TagsApi,

    /**
    * The TransactionsApi service constructor.
    * @property {module:api/TransactionsApi}
    */
    TransactionsApi
};
