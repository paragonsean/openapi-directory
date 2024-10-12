/**
 * Developer documentation
 * # Welcome  Implementing a new tool can be daunting, but it doesn't have to. You can implement journy.io in a few different ways to ensure it fits with the rest of your tech stack seamlessly.  We welcome your feedback, ideas and suggestions. We really want to make your life easier, so if we’re falling short or should be doing something different, we want to hear about it. Send us an email at [hi@journy.io](mailto:hi@journy.io) or reach out via the chat on our website or on our platform.  There are multiple ways you can send us data about users and accounts. We have both frontend and backend APIs, which can be used together at the same time.  If you already use [Segment](https://segment.com/), you can [get up and running with journy.io in seconds](https://help.journy.io/en/articles/6488307-the-segment-connector).  # Concepts  ## Users  The most basic entity is a user, a specific individual that completed an interaction with your product.  We support multiple types of users, often differentiated by it's external ID prefix. E.g. In the case you are building an ordering app, there could easily be an administrator (who updates products and checks for orders) and the end-customers who place orders. One could have a typical ADM-XXXXXXXX ID, while the other would be referenced by USR-XXXXXXXXX.  ## Accounts  In B2B SaaS, users can be part of multiple accounts. E.g. Imagine you're building a content scheduling app where an agency can manage the social media posts of their clients. Each client of the agency has its own account in the product.  If your app doesn't have the concept of a team or group of users, you can ignore accounts.  ## Events  An event is a data point that represents an interaction between a user and/or an account; and your product. Events can represents any range of interactions. E.g. Every time a customer creates an invoice in an invoicing app. Actions like creating an invoice can be tracked as an event in journy.io.  It's critical to track events properly. You'll need to provide either an account ID, or a user ID, or both; when tracking an event. E.g. If a user updates his personal settings, you can omit the account ID as the event would not be related to any account. In a same logic, an account could get a 'suspend account' event (with account ID) from an internal process, whereas no user would be associated. In most cases, events will be associated to both 1 user and 1 account.  You can optionally pass extra details as metadata (e.g. amount of the invoice). This gets particarly powerfull when creating computed properties on those event metadata. E.g. Our above ordering app could send journy.io 'Place Order' events with metadata 'price', on which journy.io very easily would compute a total order value (for each account) for the last 30 days.  💡 Metadata does not update the properties of a user or account.  # Frontend vs backend  The best implementations we see employ a hybrid approach to maximize data quality while maintaining the flexibility to easily collect the data they need.  We recommend using our JavaScript snippet to track screen views and our backend API to sync users, sync accounts and track events.  When evaluating how to track a particular event, we suggest starting with server-side and only use frontend if it's not possible to collect purely server-side. This can be the case if you need to track interactions with your product that don't result in any natural server requests (such as a button click that opens a modal).  # Frontend  ## Setup  💡 You can find the JavaScript snippet in the website settings in the connections view.  Copy the JavaScript snippet and place it in the head or body of your application.  The snippet automatically calls `journy(\"init\", { ... })` and `journy(\"pageview\")`.  ## Identify user  💡 A user ID should be a robust, static, unique identifier that you recognize a user by in your own systems. Because these IDs are consistent across a customer’s lifetime, you should include a user ID in identify calls as often as you can. Ideally, the user ID should be a database ID.  💡 journy.io does not recommend using simple email addresses or usernames as user ID, as these can change over time. journy.io recommends that you use static IDs instead, so the IDs never change. When you use a static ID, you can still recognize the user in your analytics tools, even if the user changes their email address.  💡 The properties `full_name`, `first_name`, `last_name`, `phone` and `registered_at` will be used for creating contacts in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"identify\")` allows you to identify the user that is currently using your product.  ```ts journy(\"identify\", {   // Email or user ID is required   email: \"john.doe@acme.com\",   // Unique identifier for the user in your database   userId: \"20\",    // Optional   // Hash of the user ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     full_name: \"John Doe\",     // or     first_name: \"John\",     last_name: \"Doe\",      phone: \"123\",     registered_at: new Date(/_* ... *_/),     is_admin: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Identify account  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  💡 The properties `name`, `mrr`, `plan` and `registered_at` will be used to create companies in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"account\")` allows you to identify the business account (i.e. organization) using your product.  ```ts journy(\"account\", {   // Required   // Unique identifier for the account in your database   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     name: \"ACME, Inc\",     mrr: 399,     plan: \"Pro\",     registered_at: new Date(/_* ... *_/),     is_paying: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Send page view  💡 In applications, we advise you to use screen views instead of page views.  The JavaScript snippet in the site settings includes a `pageview` by default.  ```ts journy(\"pageview\"); ```  If you have a B2B application, we recommend to set account ID for every page view that happens within the context of an account.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"pageview\", {   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Send screen view  In applications, we strongly advise you to use screen views instead of page views.  Page URLs in applications often include the account ID (e.g. https://app.acme.com/accountId/settings).  This makes it difficult to create signals, segments, ... based on those URLs.  That's what screen views solve. It allows you to set a name for the screen being viewed (e.g. Account settings).  ```ts journy(\"screen\", { name: \"Personal settings\" }); ```  If you have a B2B application, we recommend to set account ID for every screen view that happens within the context of an account.  Example: \"Personal settings\" would be without account ID, \"Team settings\" would be with account ID.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"screen\", {   name: \"Account settings\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Trigger an event  💡 Use past tense for event names.  User events:  ```js journy(\"event\", {   // required   name: \"signed_in\",    // optional   metadata: {     key: \"value\",   }, }); ```  Account events:  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```js journy(\"event\", {   // required   name: \"created_invoice\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // optional   metadata: {     key: \"value\",     amount: 100,     allow_wire_transfer: true,   }, }); ```  ## Identity verification  Identity verification ensures that one person can't impersonate another.  Identity verification requires you to add an hash (HMAC) (that you generate on your server using SHA256) to your installation snippet alongside your user ID and account ID.  journy.io won't accept requests for a logged-in user without a valid hash. The hash is calculated using a secret key, which you should never share. Without this secret key, no third party can send journy.io a valid hash for one of your users, so they can't impersonate your users.  This is optional but highly recommended.  You can enable identify verification in the website settings in the connections view.  ```js journy(\"identify\", {   userId: \"userId\",   verification: \"USER_ID_HMAC_VALUE_HERE\" })  journy(\"account\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" })  journy(\"event\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" }) ```  ### PHP  ```php <?php  hash_hmac(   'sha256', // hash function   id, // user or account ID   'secret' // secret key (keep safe!) ); ```  ### Node.js  ```js import { createHmac } from \"crypto\"  createHmac(   \"sha256\", // hash function   'secret' // secret key (keep safe!) ).update(id).digest(\"hex\") // user or account ID ```  ### Ruby  ```ruby OpenSSL::HMAC.hexdigest(   'sha256', # hash function   'secret', # secret key (keep safe!)   id.to_s # user or account ID ) ```  ### Python  ``` import hmac import hashlib  hmac.new(   b'secret', # secret key (keep safe!)   bytes(id, encoding='utf-8'), # user or account ID   digestmod=hashlib.sha256 # hash function ).hexdigest() ```  ## Single page application  You can use our JavaScript snippet inside single page applications.  You should call `journy(\"screen\")` (or `journy(\"pageview\")`) whenever a user in your application transitions to another page. You can do this by listening to router change events. The current page URL will always be resolved using `window.location.href`.  You can trigger events using `journy(\"event\")` whenever you need to.  ### Next.js  We built a demo app with Next.js. You can find the code [here](https://github.com/journy-io/js-sdk-demo-app).  This [component](https://github.com/journy-io/js-sdk-demo-app/blob/main/components/Journy.js) should be a great start.  You can use the `Script` component from Next.js to load the web snippet and call `init`.  Don't forget to listen on route changes. You can use the `useRouter` hook for that.  ### React Router v6  You can use the [`useLocation`](https://reactrouter.com/docs/en/v6/api#uselocation) hook to listen for route changes:  ```js import React, { useEffect } from \"react\"; import { useLocation } from 'react-router-dom';  function App() {   const location = useLocation();    useEffect(() => {     journy(\"screen\", { name: \"name\" });     // or     journy(\"pageview\");   }, [location]);    return (       // ...   ); } ```  ### Vue Router  You can use [`router.afterEach`](https://router.vuejs.org/guide/advanced/navigation-guards.html#global-after-hooks) to listen for route changes:  ```js const router = new VueRouter({ ... });  router.afterEach((to, from) => {   journy(\"screen\", { name: \"name\" });   // or   journy(\"pageview\"); }); ```  Note: We don't accept a page URL argument for `journy(\"pageview\")`. The current page URL will always be resolved using `window.location.href`.  ## TypeScript  We published an [npm package](https://www.npmjs.com/package/@journyio/web-types) with type definitions to enable type-safe usage of our JavaScript snippet. The code and documentation is available on [GitHub](https://github.com/journy-io/web-types).  ## Localhost  By default a site doesn't allow page views from other domains than the registered domain. This makes it difficult to test your tracking implementation locally.  You can enable \"Allow any domain\" in the site settings to disable the domain check.  This will allow you to test the JavaScript snippet with localhost as hostname.  # Backend  The journy.io API is organized around REST. Our API has predictable resource-oriented URLs, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The API is hosted on api.journy.io.  ## Official SDKs  Our SDKs are designed to help you interact with our APIs with less friction. They are written in several different languages and help bridge the gap between your application and journy.io APIs. They take away the need to know the exact URL and HTTP method to use for each API call among other things leaving you more time to focus on making your application.  | Language   | Package                                                                        | Source code                                                                | |------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------| | 💚 Node.js | [npm install @journyio/sdk ](https://www.npmjs.com/package/@journyio/sdk)      | [github.com/journy-io/js-sdk](https://github.com/journy-io/js-sdk)         | | 🐘 PHP     | [composer require journy-io/sdk](https://packagist.org/packages/journy-io/sdk) | [github.com/journy-io/php-sdk](https://github.com/journy-io/php-sdk)       | | 🐍 Python  | [pip install journyio-sdk](https://pypi.org/project/journyio-sdk/)             | [github.com/journy-io/python-sdk](https://github.com/journy-io/python-sdk) | | 💎 Ruby    | Coming soon                                                                    | Coming soon                                                                |  Your favourite programming language not included? [Let us know!](mailto:hi@journy.io)  In the meanwhile, you can use [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) to generate a client for your programming language.  ## Authentication  The journy.io API uses API keys to authenticate requests. You can view and manage your API keys in the [connections screen](https://system.journy.io).  Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  For every request send to the API we expect a header `X-Api-Key` to be set with the API Key.  ## Permissions  When creating an API Key in [the application](https://system.journy.io) you will have the choice to give permissions to an API Key (which you can change later on). These permissions restrict the API Key from different actions. When an API Key tries to perform a certain action it doesn't have the permissions for, you will receive a `401: Unauthorized` response.  ## Rate limiting  To prevent abuse of the API there is a maximum throughput of 1800 requests per minute. If you need a higher throughput, please contact us.  To keep our platform healthy and stable, we'll block API keys that consistently hit our rate limits. Therefore, please consider taking this throughput into account.  In every response the headers `X-RateLimit-Limit` and `X-RateLimit-Remaining` will be set. The `X-RateLimit-Limit`-header will always contain the current limit of requests per minute. The `X-RateLimit-Remaining`-header will always contain the amount of requests you have left in the current sliding window.  💡 The client-side tracking uses different rate limits.  ## Errors  journy.io uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g. a required parameter was omitted). Codes in the 5xx range indicate an error with journy.io's servers (these are rare).  When performing a `POST`- or `PUT`-request with a requestBody, or when including parameters, these parameters and fields will automatically be checked and validated against the API Spec. When any error occurs, you will get a response with an `errors`-field, structured as follows:  ```json {   \"errors\": {     \"parameters\": {       \"header\": {         \"headerParameterName\": \"Describe what's wrong with the header parameter.\",         ...       },       \"query\": {         \"queryParameterName\": \"Describe what's wrong with the query parameter.\",         ...       },       \"path\": {         \"pathParameterName\": \"Describe what's wrong with the path parameter.\",         ...       },     },     \"fields\": {       \"fieldName\": \"Describe what's wrong with the fieldName.\",       \"object.fieldName\": \"Describe what's wrong with the fieldName of the included object.\",        ...     }   } } ```  ## Best practices  ### Track accounts & users immediately on creation  When you create an account in your database, immediately sending data about that account to journy.io helps your team stay in sync. The same goes for users. Call [Upsert account](#operation/upsertAccount) as soon as possible, right after the account is first created in your database.  ### Update account data daily  Not every account is active every day. But, you may have properties on the account that change through background processing. That's why we recommend updating every one of your accounts' data in a recurring daily process. This way, you know that your accounts are updated every day in journy.io.  ## Changelog  ### December 2021  [POST /events](#operation/trackJourneyEvent) will be moved to [POST /track](#operation/trackEvent). [POST /events](#operation/trackJourneyEvent) is deprecated and will be removed in the future.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hi@journy.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include <QBuffer>
#include <QDateTime>
#include <QDir>
#include <QFileInfo>
#include <QTimer>
#include <QUrl>
#include <QUuid>
#include <QtGlobal>


#include "OAIHttpRequest.h"

namespace OpenAPI {

OAIHttpRequestInput::OAIHttpRequestInput() {
    initialize();
}

OAIHttpRequestInput::OAIHttpRequestInput(QString v_url_str, QString v_http_method) {
    initialize();
    url_str = v_url_str;
    http_method = v_http_method;
}

void OAIHttpRequestInput::initialize() {
    var_layout = NOT_SET;
    url_str = "";
    http_method = "GET";
}

void OAIHttpRequestInput::add_var(QString key, QString value) {
    vars[key] = value;
}

void OAIHttpRequestInput::add_file(QString variable_name, QString local_filename, QString request_filename, QString mime_type) {
    OAIHttpFileElement file;
    file.variable_name = variable_name;
    file.local_filename = local_filename;
    file.request_filename = request_filename;
    file.mime_type = mime_type;
    files.append(file);
}

OAIHttpRequestWorker::OAIHttpRequestWorker(QObject *parent, QNetworkAccessManager *_manager)
    : QObject(parent), manager(_manager), timeOutTimer(this), isResponseCompressionEnabled(false), isRequestCompressionEnabled(false), httpResponseCode(-1) {

#if QT_VERSION >= QT_VERSION_CHECK(5, 15, 0)
    randomGenerator = QRandomGenerator(QDateTime::currentDateTime().toSecsSinceEpoch());
#else
    qsrand(QDateTime::currentDateTime().toTime_t());
#endif

    if (manager == nullptr) {
        manager = new QNetworkAccessManager(this);
    }
    workingDirectory = QDir::currentPath();
    timeOutTimer.setSingleShot(true);
}

OAIHttpRequestWorker::~OAIHttpRequestWorker() {
    QObject::disconnect(&timeOutTimer, &QTimer::timeout, nullptr, nullptr);
    timeOutTimer.stop();
    for (const auto &item : multiPartFields) {
        if (item != nullptr) {
            delete item;
        }
    }
}

QMap<QString, QString> OAIHttpRequestWorker::getResponseHeaders() const {
    return headers;
}

OAIHttpFileElement OAIHttpRequestWorker::getHttpFileElement(const QString &fieldname) {
    if (!files.isEmpty()) {
        if (fieldname.isEmpty()) {
            return files.first();
        } else if (files.contains(fieldname)) {
            return files[fieldname];
        }
    }
    return OAIHttpFileElement();
}

QByteArray *OAIHttpRequestWorker::getMultiPartField(const QString &fieldname) {
    if (!multiPartFields.isEmpty()) {
        if (fieldname.isEmpty()) {
            return multiPartFields.first();
        } else if (multiPartFields.contains(fieldname)) {
            return multiPartFields[fieldname];
        }
    }
    return nullptr;
}

void OAIHttpRequestWorker::setTimeOut(int timeOutMs) {
    timeOutTimer.setInterval(timeOutMs);
    if(timeOutTimer.interval() == 0) {
        QObject::disconnect(&timeOutTimer, &QTimer::timeout, nullptr, nullptr);
    }
}

void OAIHttpRequestWorker::setWorkingDirectory(const QString &path) {
    if (!path.isEmpty()) {
        workingDirectory = path;
    }
}

void OAIHttpRequestWorker::setResponseCompressionEnabled(bool enable) {
    isResponseCompressionEnabled = enable;
}

void OAIHttpRequestWorker::setRequestCompressionEnabled(bool enable) {
    isRequestCompressionEnabled = enable;
}

int  OAIHttpRequestWorker::getHttpResponseCode() const{
    return httpResponseCode;
}

QString OAIHttpRequestWorker::http_attribute_encode(QString attribute_name, QString input) {
    // result structure follows RFC 5987
    bool need_utf_encoding = false;
    QString result = "";
    QByteArray input_c = input.toLocal8Bit();
    char c;
    for (int i = 0; i < input_c.length(); i++) {
        c = input_c.at(i);
        if (c == '\\' || c == '/' || c == '\0' || c < ' ' || c > '~') {
            // ignore and request utf-8 version
            need_utf_encoding = true;
        } else if (c == '"') {
            result += "\\\"";
        } else {
            result += c;
        }
    }

    if (result.length() == 0) {
        need_utf_encoding = true;
    }

    if (!need_utf_encoding) {
        // return simple version
        return QString("%1=\"%2\"").arg(attribute_name, result);
    }

    QString result_utf8 = "";
    for (int i = 0; i < input_c.length(); i++) {
        c = input_c.at(i);
        if ((c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) {
            result_utf8 += c;
        } else {
            result_utf8 += "%" + QString::number(static_cast<unsigned char>(input_c.at(i)), 16).toUpper();
        }
    }

    // return enhanced version with UTF-8 support
    return QString("%1=\"%2\"; %1*=utf-8''%3").arg(attribute_name, result, result_utf8);
}

void OAIHttpRequestWorker::execute(OAIHttpRequestInput *input) {

    // reset variables
    QNetworkReply *reply = nullptr;
    QByteArray request_content = "";
    response = "";
    error_type = QNetworkReply::NoError;
    error_str = "";
    bool isFormData = false;

    // decide on the variable layout

    if (input->files.length() > 0) {
        input->var_layout = MULTIPART;
    }
    if (input->var_layout == NOT_SET) {
        input->var_layout = input->http_method == "GET" || input->http_method == "HEAD" ? ADDRESS : URL_ENCODED;
    }

    // prepare request content

    QString boundary = "";

    if (input->var_layout == ADDRESS || input->var_layout == URL_ENCODED) {
        // variable layout is ADDRESS or URL_ENCODED

        if (input->vars.count() > 0) {
            bool first = true;
            isFormData = true;
            for (QString key : input->vars.keys()) {
                if (!first) {
                    request_content.append("&");
                }
                first = false;

                request_content.append(QUrl::toPercentEncoding(key));
                request_content.append("=");
                request_content.append(QUrl::toPercentEncoding(input->vars.value(key)));
            }

            if (input->var_layout == ADDRESS) {
                input->url_str += "?" + request_content;
                request_content = "";
            }
        }
    } else {
        // variable layout is MULTIPART

        boundary = QString("__-----------------------%1%2")
                    #if QT_VERSION >= QT_VERSION_CHECK(5, 15, 0)
                            .arg(QDateTime::currentDateTime().toSecsSinceEpoch())
                            .arg(randomGenerator.generate());
                    #else
                            .arg(QDateTime::currentDateTime().toTime_t())
                            .arg(qrand());
                    #endif
        QString boundary_delimiter = "--";
        QString new_line = "\r\n";

        // add variables
        for (QString key : input->vars.keys()) {
            // add boundary
            request_content.append(boundary_delimiter.toUtf8());
            request_content.append(boundary.toUtf8());
            request_content.append(new_line.toUtf8());

            // add header
            request_content.append("Content-Disposition: form-data; ");
            request_content.append(http_attribute_encode("name", key).toUtf8());
            request_content.append(new_line.toUtf8());
            request_content.append("Content-Type: text/plain");
            request_content.append(new_line.toUtf8());

            // add header to body splitter
            request_content.append(new_line.toUtf8());

            // add variable content
            request_content.append(input->vars.value(key).toUtf8());
            request_content.append(new_line.toUtf8());
        }

        // add files
        for (QList<OAIHttpFileElement>::iterator file_info = input->files.begin(); file_info != input->files.end(); file_info++) {
            QFileInfo fi(file_info->local_filename);

            // ensure necessary variables are available
            if (file_info->local_filename == nullptr
                || file_info->local_filename.isEmpty()
                || file_info->variable_name == nullptr
                || file_info->variable_name.isEmpty()
                || !fi.exists()
                || !fi.isFile()
                || !fi.isReadable()) {
                // silent abort for the current file
                continue;
            }

            QFile file(file_info->local_filename);
            if (!file.open(QIODevice::ReadOnly)) {
                // silent abort for the current file
                continue;
            }

            // ensure filename for the request
            if (file_info->request_filename == nullptr || file_info->request_filename.isEmpty()) {
                file_info->request_filename = fi.fileName();
                if (file_info->request_filename.isEmpty()) {
                    file_info->request_filename = "file";
                }
            }

            // add boundary
            request_content.append(boundary_delimiter.toUtf8());
            request_content.append(boundary.toUtf8());
            request_content.append(new_line.toUtf8());

            // add header
            request_content.append(
                QString("Content-Disposition: form-data; %1; %2").arg(http_attribute_encode("name", file_info->variable_name), http_attribute_encode("filename", file_info->request_filename)).toUtf8());
            request_content.append(new_line.toUtf8());

            if (file_info->mime_type != nullptr && !file_info->mime_type.isEmpty()) {
                request_content.append("Content-Type: ");
                request_content.append(file_info->mime_type.toUtf8());
                request_content.append(new_line.toUtf8());
            }

            request_content.append("Content-Transfer-Encoding: binary");
            request_content.append(new_line.toUtf8());

            // add header to body splitter
            request_content.append(new_line.toUtf8());

            // add file content
            request_content.append(file.readAll());
            request_content.append(new_line.toUtf8());

            file.close();
        }

        // add end of body
        request_content.append(boundary_delimiter.toUtf8());
        request_content.append(boundary.toUtf8());
        request_content.append(boundary_delimiter.toUtf8());
    }

    if (input->request_body.size() > 0) {
        qDebug() << "got a request body";
        request_content.clear();
        if(!isFormData && (input->var_layout != MULTIPART) && isRequestCompressionEnabled){
            request_content.append(compress(input->request_body, 7, OAICompressionType::Gzip));
        } else {
            request_content.append(input->request_body);
        }
    }
    // prepare connection

    QNetworkRequest request = QNetworkRequest(QUrl(input->url_str));
    if (OAIHttpRequestWorker::sslDefaultConfiguration != nullptr) {
        request.setSslConfiguration(*OAIHttpRequestWorker::sslDefaultConfiguration);
    }
    request.setRawHeader("User-Agent", "OpenAPI-Generator/1.0.0/cpp-qt");
    for (QString key : input->headers.keys()) { request.setRawHeader(key.toStdString().c_str(), input->headers.value(key).toStdString().c_str()); }

    if (request_content.size() > 0 && !isFormData && (input->var_layout != MULTIPART)) {
        if (!input->headers.contains("Content-Type")) {
            request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");
        } else {
            request.setHeader(QNetworkRequest::ContentTypeHeader, input->headers.value("Content-Type"));
        }
        if(isRequestCompressionEnabled){
            request.setRawHeader("Content-Encoding", "gzip");
        }
    } else if (input->var_layout == URL_ENCODED) {
        request.setHeader(QNetworkRequest::ContentTypeHeader, "application/x-www-form-urlencoded");
    } else if (input->var_layout == MULTIPART) {
        request.setHeader(QNetworkRequest::ContentTypeHeader, "multipart/form-data; boundary=" + boundary);
    }

    if(isResponseCompressionEnabled){
        request.setRawHeader("Accept-Encoding", "gzip");
    } else {
        request.setRawHeader("Accept-Encoding", "identity");
    }

    if (input->http_method == "GET") {
        reply = manager->get(request);
    } else if (input->http_method == "POST") {
        reply = manager->post(request, request_content);
    } else if (input->http_method == "PUT") {
        reply = manager->put(request, request_content);
    } else if (input->http_method == "HEAD") {
        reply = manager->head(request);
    } else if (input->http_method == "DELETE") {
        reply = manager->deleteResource(request);
    } else {
#if (QT_VERSION >= 0x050800)
        reply = manager->sendCustomRequest(request, input->http_method.toLatin1(), request_content);
#else
        QBuffer *buffer = new QBuffer;
        buffer->setData(request_content);
        buffer->open(QIODevice::ReadOnly);

        reply = manager->sendCustomRequest(request, input->http_method.toLatin1(), buffer);
        buffer->setParent(reply);
#endif
    }
    if (reply != nullptr) {
        reply->setParent(this);
        connect(reply, &QNetworkReply::downloadProgress, this, &OAIHttpRequestWorker::downloadProgress);
        connect(reply, &QNetworkReply::finished, [this, reply] {
            on_reply_finished(reply);
        });
    }
    if (timeOutTimer.interval() > 0) {
        QObject::connect(&timeOutTimer, &QTimer::timeout, [this, reply] {
            on_reply_timeout(reply);
        });
        timeOutTimer.start();
    }
}

void OAIHttpRequestWorker::on_reply_finished(QNetworkReply *reply) {
    bool codeSts = false;
    if(timeOutTimer.isActive()) {
        QObject::disconnect(&timeOutTimer, &QTimer::timeout, nullptr, nullptr);
        timeOutTimer.stop();
    }
    error_type = reply->error();
    error_str = reply->errorString();
    if (reply->rawHeaderPairs().count() > 0) {
        for (const auto &item : reply->rawHeaderPairs()) {
            headers.insert(item.first, item.second);
        }
    }
    auto rescode = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute).toInt(&codeSts);
    if(codeSts){
        httpResponseCode = rescode;
    } else{
        httpResponseCode = -1;
    }
    process_response(reply);
    reply->deleteLater();
    Q_EMIT on_execution_finished(this);
}

void OAIHttpRequestWorker::on_reply_timeout(QNetworkReply *reply) {
    error_type = QNetworkReply::TimeoutError;
    response = "";
    error_str = "Timed out waiting for response";
    disconnect(reply, nullptr, nullptr, nullptr);
    reply->abort();
    reply->deleteLater();
    Q_EMIT on_execution_finished(this);
}

void OAIHttpRequestWorker::process_response(QNetworkReply *reply) {
    QString contentDispositionHdr;
    QString contentTypeHdr;
    QString contentEncodingHdr;

    for(auto hdr: getResponseHeaders().keys()){
        if(hdr.compare(QString("Content-Disposition"), Qt::CaseInsensitive) == 0){
            contentDispositionHdr = getResponseHeaders().value(hdr);
        }
        if(hdr.compare(QString("Content-Type"), Qt::CaseInsensitive) == 0){
            contentTypeHdr = getResponseHeaders().value(hdr);
        }
        if(hdr.compare(QString("Content-Encoding"), Qt::CaseInsensitive) == 0){
            contentEncodingHdr = getResponseHeaders().value(hdr);
        }
    }

    if (!contentDispositionHdr.isEmpty()) {
        auto contentDisposition = contentDispositionHdr.split(QString(";"), Qt::SkipEmptyParts);
        auto contentType =
            !contentTypeHdr.isEmpty() ? contentTypeHdr.split(QString(";"), Qt::SkipEmptyParts).first() : QString();
        if ((contentDisposition.count() > 0) && (contentDisposition.first() == QString("attachment"))) {
            QString filename = QUuid::createUuid().toString();
            for (const auto &file : contentDisposition) {
                if (file.contains(QString("filename"))) {
                    filename = file.split(QString("="), Qt::SkipEmptyParts).at(1);
                    break;
                }
            }
            OAIHttpFileElement felement;
            felement.saveToFile(QString(), workingDirectory + QDir::separator() + filename, filename, contentType, reply->readAll());
            files.insert(filename, felement);
        }

    } else if (!contentTypeHdr.isEmpty()) {
        auto contentType = contentTypeHdr.split(QString(";"), Qt::SkipEmptyParts);
        if ((contentType.count() > 0) && (contentType.first() == QString("multipart/form-data"))) {
            // TODO : Handle Multipart responses
        } else {
            if(!contentEncodingHdr.isEmpty()){
                auto encoding = contentEncodingHdr.split(QString(";"), Qt::SkipEmptyParts);
                if(encoding.count() > 0){
                    auto compressionTypes = encoding.first().split(',', Qt::SkipEmptyParts);
                    if(compressionTypes.contains("gzip", Qt::CaseInsensitive) || compressionTypes.contains("deflate", Qt::CaseInsensitive)){
                        response = decompress(reply->readAll());
                    } else if(compressionTypes.contains("identity", Qt::CaseInsensitive)){
                        response = reply->readAll();
                    }
                }
            }
            else {
                response = reply->readAll();
            }
        }
    }
}

QByteArray OAIHttpRequestWorker::decompress(const QByteArray& data){
    
    Q_UNUSED(data);
    return QByteArray();
}

QByteArray OAIHttpRequestWorker::compress(const QByteArray& input, int level, OAICompressionType compressType) {
    
    Q_UNUSED(input);
    Q_UNUSED(level);
    Q_UNUSED(compressType);
    return QByteArray();
}

QSslConfiguration *OAIHttpRequestWorker::sslDefaultConfiguration;

} // namespace OpenAPI
