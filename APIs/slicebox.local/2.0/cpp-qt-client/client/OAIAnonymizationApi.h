/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIAnonymizationApi_H
#define OAI_OAIAnonymizationApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAnonymizationData.h"
#include "OAIAnonymizationKey.h"
#include "OAIAnonymizationKeyQuery.h"
#include "OAIAnonymizationKeyValue.h"
#include "OAIConfidentialityOption.h"
#include "OAIImage.h"
#include "OAIImageTagValues.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAnonymizationApi : public QObject {
    Q_OBJECT

public:
    OAIAnonymizationApi(const int timeOut = 0);
    ~OAIAnonymizationApi();

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
    * @param[in]  query QList<OAIImageTagValues> [required]
    */
    virtual void anonymizationAnonymizePost(const QList<OAIImageTagValues> &query);


    virtual void anonymizationKeysExportCsvGet();

    /**
    * @param[in]  startindex qint64 [optional]
    * @param[in]  count qint64 [optional]
    * @param[in]  orderby QString [optional]
    * @param[in]  orderascending bool [optional]
    * @param[in]  filter QString [optional]
    */
    virtual void anonymizationKeysGet(const ::OpenAPI::OptionalParam<qint64> &startindex = ::OpenAPI::OptionalParam<qint64>(), const ::OpenAPI::OptionalParam<qint64> &count = ::OpenAPI::OptionalParam<qint64>(), const ::OpenAPI::OptionalParam<QString> &orderby = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &orderascending = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void anonymizationKeysIdDelete(const qint64 &id);

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void anonymizationKeysIdGet(const qint64 &id);

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void anonymizationKeysIdKeyvaluesGet(const qint64 &id);

    /**
    * @param[in]  query OAIAnonymizationKeyQuery [required]
    */
    virtual void anonymizationKeysQueryPost(const OAIAnonymizationKeyQuery &query);


    virtual void anonymizationOptionsGet();

    /**
    * @param[in]  id qint64 [required]
    * @param[in]  tag_values OAIAnonymizationData [required]
    */
    virtual void imagesIdAnonymizePut(const qint64 &id, const OAIAnonymizationData &tag_values);

    /**
    * @param[in]  id qint64 [required]
    * @param[in]  tag_values OAIAnonymizationData [required]
    */
    virtual void imagesIdAnonymizedPost(const qint64 &id, const OAIAnonymizationData &tag_values);


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

    void anonymizationAnonymizePostCallback(OAIHttpRequestWorker *worker);
    void anonymizationKeysExportCsvGetCallback(OAIHttpRequestWorker *worker);
    void anonymizationKeysGetCallback(OAIHttpRequestWorker *worker);
    void anonymizationKeysIdDeleteCallback(OAIHttpRequestWorker *worker);
    void anonymizationKeysIdGetCallback(OAIHttpRequestWorker *worker);
    void anonymizationKeysIdKeyvaluesGetCallback(OAIHttpRequestWorker *worker);
    void anonymizationKeysQueryPostCallback(OAIHttpRequestWorker *worker);
    void anonymizationOptionsGetCallback(OAIHttpRequestWorker *worker);
    void imagesIdAnonymizePutCallback(OAIHttpRequestWorker *worker);
    void imagesIdAnonymizedPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void anonymizationAnonymizePostSignal(QList<OAIImage> summary);
    void anonymizationKeysExportCsvGetSignal(QString summary);
    void anonymizationKeysGetSignal(QList<OAIAnonymizationKey> summary);
    void anonymizationKeysIdDeleteSignal();
    void anonymizationKeysIdGetSignal(OAIAnonymizationKey summary);
    void anonymizationKeysIdKeyvaluesGetSignal(QList<OAIAnonymizationKeyValue> summary);
    void anonymizationKeysQueryPostSignal(QList<OAIAnonymizationKey> summary);
    void anonymizationOptionsGetSignal(QList<OAIConfidentialityOption> summary);
    void imagesIdAnonymizePutSignal(OAIImage summary);
    void imagesIdAnonymizedPostSignal();


    void anonymizationAnonymizePostSignalFull(OAIHttpRequestWorker *worker, QList<OAIImage> summary);
    void anonymizationKeysExportCsvGetSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void anonymizationKeysGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIAnonymizationKey> summary);
    void anonymizationKeysIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void anonymizationKeysIdGetSignalFull(OAIHttpRequestWorker *worker, OAIAnonymizationKey summary);
    void anonymizationKeysIdKeyvaluesGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIAnonymizationKeyValue> summary);
    void anonymizationKeysQueryPostSignalFull(OAIHttpRequestWorker *worker, QList<OAIAnonymizationKey> summary);
    void anonymizationOptionsGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIConfidentialityOption> summary);
    void imagesIdAnonymizePutSignalFull(OAIHttpRequestWorker *worker, OAIImage summary);
    void imagesIdAnonymizedPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use anonymizationAnonymizePostSignalError() instead")
    void anonymizationAnonymizePostSignalE(QList<OAIImage> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationAnonymizePostSignalError(QList<OAIImage> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysExportCsvGetSignalError() instead")
    void anonymizationKeysExportCsvGetSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysExportCsvGetSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysGetSignalError() instead")
    void anonymizationKeysGetSignalE(QList<OAIAnonymizationKey> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysGetSignalError(QList<OAIAnonymizationKey> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysIdDeleteSignalError() instead")
    void anonymizationKeysIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysIdGetSignalError() instead")
    void anonymizationKeysIdGetSignalE(OAIAnonymizationKey summary, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysIdGetSignalError(OAIAnonymizationKey summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysIdKeyvaluesGetSignalError() instead")
    void anonymizationKeysIdKeyvaluesGetSignalE(QList<OAIAnonymizationKeyValue> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysIdKeyvaluesGetSignalError(QList<OAIAnonymizationKeyValue> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysQueryPostSignalError() instead")
    void anonymizationKeysQueryPostSignalE(QList<OAIAnonymizationKey> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysQueryPostSignalError(QList<OAIAnonymizationKey> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationOptionsGetSignalError() instead")
    void anonymizationOptionsGetSignalE(QList<OAIConfidentialityOption> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationOptionsGetSignalError(QList<OAIConfidentialityOption> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use imagesIdAnonymizePutSignalError() instead")
    void imagesIdAnonymizePutSignalE(OAIImage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void imagesIdAnonymizePutSignalError(OAIImage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use imagesIdAnonymizedPostSignalError() instead")
    void imagesIdAnonymizedPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void imagesIdAnonymizedPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use anonymizationAnonymizePostSignalErrorFull() instead")
    void anonymizationAnonymizePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationAnonymizePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysExportCsvGetSignalErrorFull() instead")
    void anonymizationKeysExportCsvGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysExportCsvGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysGetSignalErrorFull() instead")
    void anonymizationKeysGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysIdDeleteSignalErrorFull() instead")
    void anonymizationKeysIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysIdGetSignalErrorFull() instead")
    void anonymizationKeysIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysIdKeyvaluesGetSignalErrorFull() instead")
    void anonymizationKeysIdKeyvaluesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysIdKeyvaluesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationKeysQueryPostSignalErrorFull() instead")
    void anonymizationKeysQueryPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationKeysQueryPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use anonymizationOptionsGetSignalErrorFull() instead")
    void anonymizationOptionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void anonymizationOptionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use imagesIdAnonymizePutSignalErrorFull() instead")
    void imagesIdAnonymizePutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void imagesIdAnonymizePutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use imagesIdAnonymizedPostSignalErrorFull() instead")
    void imagesIdAnonymizedPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void imagesIdAnonymizedPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
