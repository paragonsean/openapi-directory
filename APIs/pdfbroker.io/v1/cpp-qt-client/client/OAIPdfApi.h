/**
 * PdfBroker.io API
 * PdfBroker.io is an api for creating pdf files from Xsl-Fo or Html and other useful pdf utilities.
 *
 * The version of the OpenAPI document: v1
 * Contact: support@pdfbroker.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPdfApi_H
#define OAI_OAIPdfApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorResponseDto.h"
#include "OAIFoRequestDto.h"
#include "OAIFoTransformRequestDto.h"
#include "OAIHttpFileElement.h"
#include "OAIImageResponseDto.h"
#include "OAIPdfConcatenationRequestDto.h"
#include "OAIPdfResponseDto.h"
#include "OAIPdfToImageRequestDto.h"
#include "OAIPdfWriteStringRequestDto.h"
#include "OAIWkHtmlToPdfRequestDto.h"
#include "OAI_api_pdf_pdfconcat_post_request.h"
#include "OAI_api_pdf_pdftoimage_post_request.h"
#include "OAI_api_pdf_pdfwritestring_post_request.h"
#include "OAI_api_pdf_xslfo_post_request.h"
#include "OAI_api_pdf_xslfowithtransform_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPdfApi : public QObject {
    Q_OBJECT

public:
    OAIPdfApi(const int timeOut = 0);
    ~OAIPdfApi();

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


    virtual void apiPdfGet();

    /**
    * @param[in]  oai_pdf_concatenation_request_dto OAIPdfConcatenationRequestDto [optional]
    */
    virtual void apiPdfPdfconcatPost(const ::OpenAPI::OptionalParam<OAIPdfConcatenationRequestDto> &oai_pdf_concatenation_request_dto = ::OpenAPI::OptionalParam<OAIPdfConcatenationRequestDto>());

    /**
    * @param[in]  oai_pdf_to_image_request_dto OAIPdfToImageRequestDto [optional]
    */
    virtual void apiPdfPdftoimagePost(const ::OpenAPI::OptionalParam<OAIPdfToImageRequestDto> &oai_pdf_to_image_request_dto = ::OpenAPI::OptionalParam<OAIPdfToImageRequestDto>());

    /**
    * @param[in]  oai_pdf_write_string_request_dto OAIPdfWriteStringRequestDto [optional]
    */
    virtual void apiPdfPdfwritestringPost(const ::OpenAPI::OptionalParam<OAIPdfWriteStringRequestDto> &oai_pdf_write_string_request_dto = ::OpenAPI::OptionalParam<OAIPdfWriteStringRequestDto>());

    /**
    * @param[in]  oaiwk_html_to_pdf_request_dto OAIWkHtmlToPdfRequestDto [optional]
    */
    virtual void apiPdfWkhtmltopdfPost(const ::OpenAPI::OptionalParam<OAIWkHtmlToPdfRequestDto> &oaiwk_html_to_pdf_request_dto = ::OpenAPI::OptionalParam<OAIWkHtmlToPdfRequestDto>());

    /**
    * @param[in]  oaifo_request_dto OAIFoRequestDto [optional]
    */
    virtual void apiPdfXslfoPost(const ::OpenAPI::OptionalParam<OAIFoRequestDto> &oaifo_request_dto = ::OpenAPI::OptionalParam<OAIFoRequestDto>());

    /**
    * @param[in]  oaifo_transform_request_dto OAIFoTransformRequestDto [optional]
    */
    virtual void apiPdfXslfowithtransformPost(const ::OpenAPI::OptionalParam<OAIFoTransformRequestDto> &oaifo_transform_request_dto = ::OpenAPI::OptionalParam<OAIFoTransformRequestDto>());


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

    void apiPdfGetCallback(OAIHttpRequestWorker *worker);
    void apiPdfPdfconcatPostCallback(OAIHttpRequestWorker *worker);
    void apiPdfPdftoimagePostCallback(OAIHttpRequestWorker *worker);
    void apiPdfPdfwritestringPostCallback(OAIHttpRequestWorker *worker);
    void apiPdfWkhtmltopdfPostCallback(OAIHttpRequestWorker *worker);
    void apiPdfXslfoPostCallback(OAIHttpRequestWorker *worker);
    void apiPdfXslfowithtransformPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiPdfGetSignal();
    void apiPdfPdfconcatPostSignal(OAIPdfResponseDto summary);
    void apiPdfPdftoimagePostSignal(OAIImageResponseDto summary);
    void apiPdfPdfwritestringPostSignal(OAIPdfResponseDto summary);
    void apiPdfWkhtmltopdfPostSignal(OAIPdfResponseDto summary);
    void apiPdfXslfoPostSignal(OAIPdfResponseDto summary);
    void apiPdfXslfowithtransformPostSignal(OAIPdfResponseDto summary);


    void apiPdfGetSignalFull(OAIHttpRequestWorker *worker);
    void apiPdfPdfconcatPostSignalFull(OAIHttpRequestWorker *worker, OAIPdfResponseDto summary);
    void apiPdfPdftoimagePostSignalFull(OAIHttpRequestWorker *worker, OAIImageResponseDto summary);
    void apiPdfPdfwritestringPostSignalFull(OAIHttpRequestWorker *worker, OAIPdfResponseDto summary);
    void apiPdfWkhtmltopdfPostSignalFull(OAIHttpRequestWorker *worker, OAIPdfResponseDto summary);
    void apiPdfXslfoPostSignalFull(OAIHttpRequestWorker *worker, OAIPdfResponseDto summary);
    void apiPdfXslfowithtransformPostSignalFull(OAIHttpRequestWorker *worker, OAIPdfResponseDto summary);

    Q_DECL_DEPRECATED_X("Use apiPdfGetSignalError() instead")
    void apiPdfGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfPdfconcatPostSignalError() instead")
    void apiPdfPdfconcatPostSignalE(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfPdfconcatPostSignalError(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfPdftoimagePostSignalError() instead")
    void apiPdfPdftoimagePostSignalE(OAIImageResponseDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfPdftoimagePostSignalError(OAIImageResponseDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfPdfwritestringPostSignalError() instead")
    void apiPdfPdfwritestringPostSignalE(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfPdfwritestringPostSignalError(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfWkhtmltopdfPostSignalError() instead")
    void apiPdfWkhtmltopdfPostSignalE(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfWkhtmltopdfPostSignalError(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfXslfoPostSignalError() instead")
    void apiPdfXslfoPostSignalE(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfXslfoPostSignalError(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfXslfowithtransformPostSignalError() instead")
    void apiPdfXslfowithtransformPostSignalE(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfXslfowithtransformPostSignalError(OAIPdfResponseDto summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiPdfGetSignalErrorFull() instead")
    void apiPdfGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfPdfconcatPostSignalErrorFull() instead")
    void apiPdfPdfconcatPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfPdfconcatPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfPdftoimagePostSignalErrorFull() instead")
    void apiPdfPdftoimagePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfPdftoimagePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfPdfwritestringPostSignalErrorFull() instead")
    void apiPdfPdfwritestringPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfPdfwritestringPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfWkhtmltopdfPostSignalErrorFull() instead")
    void apiPdfWkhtmltopdfPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfWkhtmltopdfPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfXslfoPostSignalErrorFull() instead")
    void apiPdfXslfoPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfXslfoPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiPdfXslfowithtransformPostSignalErrorFull() instead")
    void apiPdfXslfowithtransformPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiPdfXslfowithtransformPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
