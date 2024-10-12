/**
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
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
