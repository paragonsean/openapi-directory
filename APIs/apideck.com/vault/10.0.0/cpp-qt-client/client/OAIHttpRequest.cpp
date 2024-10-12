/**
 * Vault API
 * Welcome to the Vault API 👋  When you're looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  ``` curl -X POST https://unify.apideck.com/vault/sessions     -H \"Content-Type: application/json\"     -H \"Authorization: Bearer <your-api-key>\"     -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"     -H \"X-APIDECK-APP-ID: <application-id>\"     -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}' ```  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.  This is being handled by the `/authorize` endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
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
