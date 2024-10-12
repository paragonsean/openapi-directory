/**
 * PAC Control REST API
 * #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller's variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC's strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   ``` https://1.2.3.4/api/v1/device/strategy/vars/int32s ``` and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  ```json [ { \"nMyVeryFavoriteNumber\": 22 },   { \"nWidgetsProducedToday\": 22222 },   { \"DELAY_LOOP_TIME_IN_MSECS\"  : 200 } ] ``` **Read the engineering units** (EU) of an analog input point configured in the PAC's strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   `https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu`  The GET response will be a single JSON name-value pair such as: ```json { \"value\": 72.22 } ```      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
 *
 * The version of the OpenAPI document: R1.0a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * Based on http://www.creativepulse.gr/en/blog/2014/restful-api-requests-using-qt-cpp-for-linux-mac-osx-ms-windows
 * By Alex Stylianos
 *
 **/

#ifndef OAI_HTTPREQUESTWORKER_H
#define OAI_HTTPREQUESTWORKER_H

#include <QMap>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QObject>
#include <QString>
#include <QTimer>
#include <QRandomGenerator>

#include "OAIHttpFileElement.h"

namespace OpenAPI {

enum OAIHttpRequestVarLayout {
    NOT_SET,
    ADDRESS,
    URL_ENCODED,
    MULTIPART
};

class OAIHttpRequestInput {

public:
    QString url_str;
    QString http_method;
    OAIHttpRequestVarLayout var_layout;
    QMap<QString, QString> vars;
    QMap<QString, QString> headers;
    QList<OAIHttpFileElement> files;
    QByteArray request_body;

    OAIHttpRequestInput();
    OAIHttpRequestInput(QString v_url_str, QString v_http_method);
    void initialize();
    void add_var(QString key, QString value);
    void add_file(QString variable_name, QString local_filename, QString request_filename, QString mime_type);
};

class OAIHttpRequestWorker : public QObject {
    Q_OBJECT

public:
    explicit OAIHttpRequestWorker(QObject *parent = nullptr, QNetworkAccessManager *manager = nullptr);
    virtual ~OAIHttpRequestWorker();

    QByteArray response;
    QNetworkReply::NetworkError error_type;
    QString error_str;

    QMap<QString, QString> getResponseHeaders() const;
    QString http_attribute_encode(QString attribute_name, QString input);
    void execute(OAIHttpRequestInput *input);
    static QSslConfiguration *sslDefaultConfiguration;
    void setTimeOut(int timeOutMs);
    void setWorkingDirectory(const QString &path);
    OAIHttpFileElement getHttpFileElement(const QString &fieldname = QString());
    QByteArray *getMultiPartField(const QString &fieldname = QString());
    void setResponseCompressionEnabled(bool enable);
    void setRequestCompressionEnabled(bool enable);
    int  getHttpResponseCode() const;

Q_SIGNALS:
    void on_execution_finished(OAIHttpRequestWorker *worker);
    void downloadProgress(qint64 bytesReceived, qint64 bytesTotal);

private:
    enum OAICompressionType{
        Zlib,
        Gzip
    };
    QNetworkAccessManager *manager;
    QMap<QString, QString> headers;
    QMap<QString, OAIHttpFileElement> files;
    QMap<QString, QByteArray *> multiPartFields;
    QString workingDirectory;
    QTimer timeOutTimer;
    bool isResponseCompressionEnabled;
    bool isRequestCompressionEnabled;
    int  httpResponseCode;
    QRandomGenerator randomGenerator;

    void on_reply_timeout(QNetworkReply *reply);
    void on_reply_finished(QNetworkReply *reply);
    void process_response(QNetworkReply *reply);
    QByteArray decompress(const QByteArray& data);
    QByteArray compress(const QByteArray& input, int level, OAICompressionType compressType);
};

} // namespace OpenAPI

#endif // OAI_HTTPREQUESTWORKER_H
