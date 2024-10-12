/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITagsApiApi_H
#define OAI_OAITagsApiApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICustomVisionError.h"
#include "OAITag.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITagsApiApi : public QObject {
    Q_OBJECT

public:
    OAITagsApiApi(const int timeOut = 0);
    ~OAITagsApiApi();

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
    * @param[in]  project_id QString [required]
    * @param[in]  name QString [required]
    * @param[in]  training_key QString [required]
    * @param[in]  description QString [optional]
    * @param[in]  type QString [optional]
    */
    virtual void createTag(const QString &project_id, const QString &name, const QString &training_key, const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  tag_id QString [required]
    * @param[in]  training_key QString [required]
    */
    virtual void deleteTag(const QString &project_id, const QString &tag_id, const QString &training_key);

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  tag_id QString [required]
    * @param[in]  training_key QString [required]
    * @param[in]  iteration_id QString [optional]
    */
    virtual void getTag(const QString &project_id, const QString &tag_id, const QString &training_key, const ::OpenAPI::OptionalParam<QString> &iteration_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  training_key QString [required]
    * @param[in]  iteration_id QString [optional]
    */
    virtual void getTags(const QString &project_id, const QString &training_key, const ::OpenAPI::OptionalParam<QString> &iteration_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  project_id QString [required]
    * @param[in]  tag_id QString [required]
    * @param[in]  training_key QString [required]
    * @param[in]  oai_tag OAITag [required]
    */
    virtual void updateTag(const QString &project_id, const QString &tag_id, const QString &training_key, const OAITag &oai_tag);


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

    void createTagCallback(OAIHttpRequestWorker *worker);
    void deleteTagCallback(OAIHttpRequestWorker *worker);
    void getTagCallback(OAIHttpRequestWorker *worker);
    void getTagsCallback(OAIHttpRequestWorker *worker);
    void updateTagCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createTagSignal(OAITag summary);
    void deleteTagSignal();
    void getTagSignal(OAITag summary);
    void getTagsSignal(QList<OAITag> summary);
    void updateTagSignal(OAITag summary);


    void createTagSignalFull(OAIHttpRequestWorker *worker, OAITag summary);
    void deleteTagSignalFull(OAIHttpRequestWorker *worker);
    void getTagSignalFull(OAIHttpRequestWorker *worker, OAITag summary);
    void getTagsSignalFull(OAIHttpRequestWorker *worker, QList<OAITag> summary);
    void updateTagSignalFull(OAIHttpRequestWorker *worker, OAITag summary);

    Q_DECL_DEPRECATED_X("Use createTagSignalError() instead")
    void createTagSignalE(OAITag summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createTagSignalError(OAITag summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTagSignalError() instead")
    void deleteTagSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagSignalError() instead")
    void getTagSignalE(OAITag summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagSignalError(OAITag summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagsSignalError() instead")
    void getTagsSignalE(QList<OAITag> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagsSignalError(QList<OAITag> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateTagSignalError() instead")
    void updateTagSignalE(OAITag summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateTagSignalError(OAITag summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createTagSignalErrorFull() instead")
    void createTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTagSignalErrorFull() instead")
    void deleteTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagSignalErrorFull() instead")
    void getTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTagsSignalErrorFull() instead")
    void getTagsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTagsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateTagSignalErrorFull() instead")
    void updateTagSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateTagSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
