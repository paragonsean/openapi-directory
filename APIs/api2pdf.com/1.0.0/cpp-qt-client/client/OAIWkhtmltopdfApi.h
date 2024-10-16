/**
 * Api2Pdf - PDF Generation, Powered by AWS Lambda
 *  # Introduction [Api2Pdf](https://www.api2pdf.com) is a powerful PDF generation API with no rate limits or file size constraints. Api2Pdf runs on AWS Lambda, a serverless architecture powered by Amazon to scale to millions of requests while being up to 90% cheaper than alternatives. **Supports wkhtmltopdf, Headless Chrome, LibreOffice, and PDF Merge.** You can also generate barcodes with ZXING (Zebra Crossing). # SDKs & Client Libraries We've made a number of open source libraries available for the API - Python: [https://github.com/api2pdf/api2pdf.python](https://github.com/api2pdf/api2pdf.python) - .NET: [https://github.com/api2pdf/api2pdf.dotnet](https://github.com/api2pdf/api2pdf.dotnet) - Nodejs: [https://github.com/api2pdf/api2pdf.node](https://github.com/api2pdf/api2pdf.node) - PHP: [https://github.com/Api2Pdf/api2pdf.php](https://github.com/Api2Pdf/api2pdf.php) - Ruby: (Coming soon) # Authorization Create an account at [portal.api2pdf.com](https://portal.api2pdf.com/register) to get an API key.  **Authorize your API calls** - GET requests, include apikey=YOUR-API-KEY as a query string parameter - POST requests, add **Authorization** to your header. ``` Authorization: YOUR-API-KEY ```  # Quickstart If you are looking for just a quick call to grab PDFs of a URL, you can do a GET request like: ``` https://v2018.api2pdf.com/chrome/url?url={UrlToConvert}&apikey={YourApiKey} ```  For more advanced usage and settings, see the API specification below. 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@api2pdf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIWkhtmltopdfApi_H
#define OAI_OAIWkhtmltopdfApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIApiResponseFailure.h"
#include "OAIApiResponseSuccess.h"
#include "OAIHttpFileElement.h"
#include "OAIWkHtmlToPdfHtmlToPdfRequest.h"
#include "OAIWkHtmlToPdfUrlToPdfRequest.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIWkhtmltopdfApi : public QObject {
    Q_OBJECT

public:
    OAIWkhtmltopdfApi(const int timeOut = 0);
    ~OAIWkhtmltopdfApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  oaiwk_html_to_pdf_html_to_pdf_request OAIWkHtmlToPdfHtmlToPdfRequest [optional]
    */
    virtual void wkhtmltopdfFromHtmlPost(const ::OpenAPI::OptionalParam<OAIWkHtmlToPdfHtmlToPdfRequest> &oaiwk_html_to_pdf_html_to_pdf_request = ::OpenAPI::OptionalParam<OAIWkHtmlToPdfHtmlToPdfRequest>());

    /**
    * @param[in]  url QString [required]
    * @param[in]  output QString [optional]
    */
    virtual void wkhtmltopdfFromUrlGET(const QString &url, const ::OpenAPI::OptionalParam<QString> &output = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oaiwk_html_to_pdf_url_to_pdf_request OAIWkHtmlToPdfUrlToPdfRequest [optional]
    */
    virtual void wkhtmltopdfFromUrlPost(const ::OpenAPI::OptionalParam<OAIWkHtmlToPdfUrlToPdfRequest> &oaiwk_html_to_pdf_url_to_pdf_request = ::OpenAPI::OptionalParam<OAIWkHtmlToPdfUrlToPdfRequest>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void wkhtmltopdfFromHtmlPostCallback(OAIHttpRequestWorker *worker);
    void wkhtmltopdfFromUrlGETCallback(OAIHttpRequestWorker *worker);
    void wkhtmltopdfFromUrlPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void wkhtmltopdfFromHtmlPostSignal(OAIApiResponseSuccess summary);
    void wkhtmltopdfFromUrlGETSignal(OAIApiResponseSuccess summary);
    void wkhtmltopdfFromUrlPostSignal(OAIApiResponseSuccess summary);


    void wkhtmltopdfFromHtmlPostSignalFull(OAIHttpRequestWorker *worker, OAIApiResponseSuccess summary);
    void wkhtmltopdfFromUrlGETSignalFull(OAIHttpRequestWorker *worker, OAIApiResponseSuccess summary);
    void wkhtmltopdfFromUrlPostSignalFull(OAIHttpRequestWorker *worker, OAIApiResponseSuccess summary);

    Q_DECL_DEPRECATED_X("Use wkhtmltopdfFromHtmlPostSignalError() instead")
    void wkhtmltopdfFromHtmlPostSignalE(OAIApiResponseSuccess summary, QNetworkReply::NetworkError error_type, QString error_str);
    void wkhtmltopdfFromHtmlPostSignalError(OAIApiResponseSuccess summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use wkhtmltopdfFromUrlGETSignalError() instead")
    void wkhtmltopdfFromUrlGETSignalE(OAIApiResponseSuccess summary, QNetworkReply::NetworkError error_type, QString error_str);
    void wkhtmltopdfFromUrlGETSignalError(OAIApiResponseSuccess summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use wkhtmltopdfFromUrlPostSignalError() instead")
    void wkhtmltopdfFromUrlPostSignalE(OAIApiResponseSuccess summary, QNetworkReply::NetworkError error_type, QString error_str);
    void wkhtmltopdfFromUrlPostSignalError(OAIApiResponseSuccess summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use wkhtmltopdfFromHtmlPostSignalErrorFull() instead")
    void wkhtmltopdfFromHtmlPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void wkhtmltopdfFromHtmlPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use wkhtmltopdfFromUrlGETSignalErrorFull() instead")
    void wkhtmltopdfFromUrlGETSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void wkhtmltopdfFromUrlGETSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use wkhtmltopdfFromUrlPostSignalErrorFull() instead")
    void wkhtmltopdfFromUrlPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void wkhtmltopdfFromUrlPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
