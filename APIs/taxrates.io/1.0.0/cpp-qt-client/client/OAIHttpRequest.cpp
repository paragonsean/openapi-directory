/**
 * Taxrates.io API
 * <h3>Introduction</h3> <p>Taxrates.io is a global tax rate service that automates the management of monitoring tax rates changes in 181 countries. We monitor over 14,000 US sales tax, VAT, GST rates for you and make updates via our API so you always have the most update tax rates.</p> <p>You can use Taxrates.io as a virtual sandbox where we provide you with 30 days free trial.</p> <h3>Countries</h3> <p>We currently support the following countries around the world. If you would like to request the addition of a new country, please email us at <a href=\"mailto:support@taxrates.io\">support@taxrates.io</a></p> <table>   <tr><td>Afghanistan</td><td>Gambia</td><td>Nicaragua</td></tr>   <tr><td>Albania</td><td>Georgia</td><td>Niger</td></tr>   <tr><td>Andorra</td><td>Germany</td><td>Nigeria</td></tr>   <tr><td>Angola</td><td>Ghana</td><td>North Korea</td></tr>   <tr><td>Antigua and Barbuda</td><td>Greece</td><td>Norway</td></tr>   <tr><td>Argentina</td><td>Grenada</td><td>Pakistan</td></tr>   <tr><td>Armenia</td><td>Guam</td><td>Palestine</td></tr>   <tr><td>Aruba</td><td>Guatemala</td><td>Panama</td></tr>   <tr><td>Australia</td><td>Guinea</td><td>Papua New Guinea</td></tr>   <tr><td>Austria</td><td>Guyana</td><td>Paraguay</td></tr>   <tr><td>Azerbaijan</td><td>Haiti</td><td>Peru</td></tr>   <tr><td>Bahamas</td><td>Honduras</td><td>Philippines</td></tr>   <tr><td>Bangladesh</td><td>Hungary</td><td>Poland</td></tr>   <tr><td>Barbados</td><td>Iceland</td><td>Portugal</td></tr>   <tr><td>Belarus</td><td>India</td><td>Puerto Rico</td></tr>   <tr><td>Belgium</td><td>Indonesia</td><td>Republic of the Congo</td></tr>   <tr><td>Belize</td><td>Iran</td><td>Romania</td></tr>   <tr><td>Benin</td><td>Ireland</td><td>Russian Federation</td></tr>   <tr><td>Bhutan</td><td>Isle of Man</td><td>Rwanda</td></tr>   <tr><td>Bolivia</td><td>Israel</td><td>Samoa</td></tr>   <tr><td>Bonaire</td><td>Italy</td><td>Senegal</td></tr>   <tr><td>Bosnia and Herzegovina</td><td>Japan</td><td>Serbia</td></tr>   <tr><td>Botswana</td><td>Jersey</td><td>Seychelles</td></tr>   <tr><td>Brazil</td><td>Jordan</td><td>Sierra Leone</td></tr>   <tr><td>Bulgaria</td><td>Jordan</td><td>Singapore</td></tr>   <tr><td>Burkina Faso</td><td>Kazakhstan</td><td>Slovakia</td></tr>   <tr><td>Burundi</td><td>Kenya</td><td>Slovenia</td></tr>   <tr><td>Cambodia</td><td>Kiribati</td><td>Solomon Islands</td></tr>   <tr><td>Cameroon</td><td>Kosovo</td><td>Somalia</td></tr>   <tr><td>Cape Verde</td><td>Kyrgyzstan</td><td>South Africa</td></tr>   <tr><td>Central African Republic</td><td>Laos</td><td>South Korea</td></tr>   <tr><td>Chad</td><td>Latvia</td><td>South Sudan</td></tr>   <tr><td>Chile</td><td>Lebanon</td><td>Spain</td></tr>   <tr><td>China</td><td>Lesotho</td><td>Sri Lanka</td></tr>   <tr><td>Columbia</td><td>Liberia</td><td>St Lucia</td></tr>   <tr><td>Comoros</td><td>Liechtenstein</td><td>Sudan</td></tr>   <tr><td>Cook Islands</td><td>Lithuania</td><td>Suriname</td></tr>   <tr><td>Costa Rica</td><td>Luxembourg</td><td>Swaziland</td></tr>   <tr><td>Cote d'Ivoire</td><td>Macedonia</td><td>Sweden</td></tr>   <tr><td>Croatia</td><td>Madagascar</td><td>Switzerland</td></tr>   <tr><td>Cuba</td><td>Malawi</td><td>Tahiti</td></tr>   <tr><td>Curacao</td><td>Malaysia</td><td>Taiwan</td></tr>   <tr><td>Cyprus</td><td>Maldives</td><td>Tajikistan</td></tr>   <tr><td>Czech Republic</td><td>Mali</td><td>Tanzania</td></tr>   <tr><td>Democratic Republic of the Congo</td><td>Malta</td><td>Thailand</td></tr>   <tr><td>Denmark</td><td>Mauritania</td><td>Togo</td></tr>   <tr><td>Djbouti</td><td>Mauritius</td><td>Tonga</td></tr>   <tr><td>Dominica</td><td>Mexico</td><td>Trinidad and Tobago</td></tr>   <tr><td>Dominican Republic</td><td>Micronesia</td><td>Tunisia</td></tr>   <tr><td>Ecuador</td><td>Moldova</td><td>Turkmenistan</td></tr>   <tr><td>Egypt</td><td>Monaco</td><td>Tuvalu</td></tr>   <tr><td>El Salvador</td><td>Mongolia</td><td>Uganda</td></tr>   <tr><td>Equatorial Guinea</td><td>Montenegro</td><td>Ukraine</td></tr>   <tr><td>Eritrea</td><td>Morocco</td><td>United Kingdom</td></tr>   <tr><td>Estonia</td><td>Mozambique</td><td>United States</td></tr>   <tr><td>Ethiopia</td><td>Myanmar</td><td>Uruguay</td></tr>   <tr><td>Fiji</td><td>Namibia</td><td>Vanuatu</td></tr>   <tr><td>Finland</td><td>Nepal</td><td>Venezuela</td></tr>   <tr><td>France</td><td>Netherlands</td><td>Vietnam</td></tr>   <tr><td>Gabon</td><td>New Zealand</td><td>Yemen</td></tr> </table> <h3>Products codes</h3> <p>The Taxrates.io API’s provides product-level tax rates for a subset of product codes. These codes are to be used for products that are either exempt from tax in some jurisdictions or are taxed at reduced rates.</p> <p>We will be expanding support for additional, less common categories over time. If you would like to request the addition of a new product category, please email us at <a href=\"mailto:support@taxrates.io\">support@taxrates.io</a></p> <p>Please select a product code/s when making a request to the Taxrates.io API</p> <table>   <tr><th>Product code</th><th>Product Description</th></tr>   <tr><td>C010</td><td>Services which are not subject to a service-specific tax</td></tr>   <tr><td>C011</td><td>Software - Downloaded</td></tr>   <tr><td>C012</td><td>Books - Downloaded</td></tr>   <tr><td>C011</td><td>Music - Downloaded</td></tr>   <tr><td>C011</td><td>Movies/Digital Video - Downloaded</td></tr>   <tr><td>C011</td><td>Other Electronic Goods - Downloaded</td></tr>   <tr><td>C011</td><td>Streaming Music/Audio Services new</td></tr>   <tr><td>C011</td><td>Streaming Video Services new</td></tr>   <tr><td>C018</td><td>Software as a Services, Generally (Remote Access to Hosted Software)</td></tr>   <tr><td>C018</td><td>Remote Access to Hosted Software - Personal Use</td></tr>   <tr><td>C018</td><td>Remote Access to Hosted Software - Business Use</td></tr>   <tr><td>C021</td><td>Remote Access to Hosted Business Custom Applications</td></tr>   <tr><td>C021</td><td>Personal Cloud Storage/Backup</td></tr>   <tr><td>C021</td><td>Business Cloud Storage/Backup</td></tr>   <tr><td>C021</td><td>Business Data Warehouses</td></tr>   <tr><td>C022</td><td>Infrastructure as Service, Generally</td></tr>   <tr><td>C022</td><td>Ecommerce Site/Webserver Hosting</td></tr>   <tr><td>C022</td><td>Provision of Virtual Computing Capacity</td></tr>   <tr><td>C022</td><td>Software - package or canned program</td></tr>   <tr><td>C022</td><td>Software - modifications to canned program</td></tr>   <tr><td>C022</td><td>Software - custom programs - material</td></tr>   <tr><td>C022</td><td>Software - custom programs - professional serv.</td></tr>   <tr><td>C022</td><td>Information services</td></tr>   <tr><td>C022</td><td>Data processing services</td></tr>   <tr><td>C022</td><td>Mainframe computer access and processing serv.</td></tr>   <tr><td>C022</td><td>Online Data processing services</td></tr> </table> <h3>Filtering</h3> <p>When calling the API endpoints you can use 'filter' parameters to get tax rate for the selected type. You can get the following tax types (Each tax rate will always have one of following types)</p> <h3>US Sales tax Rates</h3> <ol>   <li>CombinedRate</li>   <li>StateRate</li>   <li>CountyRate</li>   <li>CityRate</li>   <li>SpecialRate</li> </ol> <p>We recommend using <a href=\"https://www.getpostman.com/\">Postman</a> when discovering our API. Happy using!</p> <h3>Rate Limiting</h3> <p>We limit API requests.</p> <p>If you’re exceeding this rate and encountering 429 errors, review the following:</p> <ul>   <li>Only make requests in states / regions where you have enabled.</li>   <li>Cache responses if the order details haven’t changed since the last calculation at checkout.</li> </ul> <h3>Errors</h3> <p>The Taxrates.io API uses the following error codes:<p/> <table>   <tr><th>Code</th><th>Error Message</th></tr>   <tr><td>400</td><td>Bad Request – Your request format is bad.</td></tr>   <tr><td>401</td><td>Unauthorized – Your API key is wrong.</td></tr>   <tr><td>404</td><td>Not Found – The specified resource could not be found.</td></tr>   <tr><td>405</td><td>Method Not Allowed – You tried to access a resource with an invalid method.</td></tr>   <tr><td>429</td><td>Too Many Requests – You’re requesting too many resources! Slow down!</td></tr>   <tr><td>500</td><td>Internal Server Error – We had a problem with our server. Try again later.</td></tr>   <tr><td>503</td><td>Service Unavailable – We’re temporarily offline for maintenance. Try again later.</td></tr> </table> <p>Verify your API token is correct and make sure you’re correctly setting the <a href=\"#authentication\">Authorization header</a>.</p> <p>If you’re still not sure what’s wrong, <a href=\"mailto:support@taxrates.io\">contact us</a> and we’ll investigate.</p> <h3>Changelog</h3> <p>Stay on top of new developer-facing features, accuracy improvements, and bug fixes for our API. Have a request? Encounter an issue? <a href=\"mailto:support@taxrates.io\">We’d love to hear your feedback.</a></p>   Contact Support:  Name: apiteam@taxrates.io
 *
 * The version of the OpenAPI document: 1.0.0
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
