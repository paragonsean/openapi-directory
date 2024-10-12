/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICommentApiApi_H
#define OAI_OAICommentApiApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICommentForApiContract.h"
#include "OAICommentForApiContractPartialFindResult.h"
#include "OAICommentOptionalFields.h"
#include "OAICommentSortRule.h"
#include "OAIContentLanguagePreference.h"
#include "OAIEntryOptionalFields.h"
#include "OAIEntryType.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICommentApiApi : public QObject {
    Q_OBJECT

public:
    OAICommentApiApi(const int timeOut = 0);
    ~OAICommentApiApi();

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
    * @param[in]  entry_type OAIEntryType [required]
    * @param[in]  comment_id qint32 [required]
    */
    virtual void apiCommentsEntryTypeCommentsCommentIdDelete(const OAIEntryType &entry_type, const qint32 &comment_id);

    /**
    * @param[in]  entry_type OAIEntryType [required]
    * @param[in]  comment_id qint32 [required]
    * @param[in]  oai_comment_for_api_contract OAICommentForApiContract [optional]
    */
    virtual void apiCommentsEntryTypeCommentsCommentIdPost(const OAIEntryType &entry_type, const qint32 &comment_id, const ::OpenAPI::OptionalParam<OAICommentForApiContract> &oai_comment_for_api_contract = ::OpenAPI::OptionalParam<OAICommentForApiContract>());

    /**
    * @param[in]  entry_type OAIEntryType [required]
    * @param[in]  entry_id qint32 [optional]
    */
    virtual void apiCommentsEntryTypeCommentsGet(const OAIEntryType &entry_type, const ::OpenAPI::OptionalParam<qint32> &entry_id = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  entry_type OAIEntryType [required]
    * @param[in]  oai_comment_for_api_contract OAICommentForApiContract [optional]
    */
    virtual void apiCommentsEntryTypeCommentsPost(const OAIEntryType &entry_type, const ::OpenAPI::OptionalParam<OAICommentForApiContract> &oai_comment_for_api_contract = ::OpenAPI::OptionalParam<OAICommentForApiContract>());

    /**
    * @param[in]  before QDateTime [optional]
    * @param[in]  since QDateTime [optional]
    * @param[in]  user_id qint32 [optional]
    * @param[in]  entry_type OAIEntryType [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  get_total_count bool [optional]
    * @param[in]  fields OAICommentOptionalFields [optional]
    * @param[in]  entry_fields OAIEntryOptionalFields [optional]
    * @param[in]  lang OAIContentLanguagePreference [optional]
    * @param[in]  sort_rule OAICommentSortRule [optional]
    */
    virtual void apiCommentsGet(const ::OpenAPI::OptionalParam<QDateTime> &before = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &since = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<qint32> &user_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIEntryType> &entry_type = ::OpenAPI::OptionalParam<OAIEntryType>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &get_total_count = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAICommentOptionalFields> &fields = ::OpenAPI::OptionalParam<OAICommentOptionalFields>(), const ::OpenAPI::OptionalParam<OAIEntryOptionalFields> &entry_fields = ::OpenAPI::OptionalParam<OAIEntryOptionalFields>(), const ::OpenAPI::OptionalParam<OAIContentLanguagePreference> &lang = ::OpenAPI::OptionalParam<OAIContentLanguagePreference>(), const ::OpenAPI::OptionalParam<OAICommentSortRule> &sort_rule = ::OpenAPI::OptionalParam<OAICommentSortRule>());


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

    void apiCommentsEntryTypeCommentsCommentIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiCommentsEntryTypeCommentsCommentIdPostCallback(OAIHttpRequestWorker *worker);
    void apiCommentsEntryTypeCommentsGetCallback(OAIHttpRequestWorker *worker);
    void apiCommentsEntryTypeCommentsPostCallback(OAIHttpRequestWorker *worker);
    void apiCommentsGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiCommentsEntryTypeCommentsCommentIdDeleteSignal();
    void apiCommentsEntryTypeCommentsCommentIdPostSignal();
    void apiCommentsEntryTypeCommentsGetSignal(OAICommentForApiContractPartialFindResult summary);
    void apiCommentsEntryTypeCommentsPostSignal(OAICommentForApiContract summary);
    void apiCommentsGetSignal(OAICommentForApiContractPartialFindResult summary);


    void apiCommentsEntryTypeCommentsCommentIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiCommentsEntryTypeCommentsCommentIdPostSignalFull(OAIHttpRequestWorker *worker);
    void apiCommentsEntryTypeCommentsGetSignalFull(OAIHttpRequestWorker *worker, OAICommentForApiContractPartialFindResult summary);
    void apiCommentsEntryTypeCommentsPostSignalFull(OAIHttpRequestWorker *worker, OAICommentForApiContract summary);
    void apiCommentsGetSignalFull(OAIHttpRequestWorker *worker, OAICommentForApiContractPartialFindResult summary);

    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsCommentIdDeleteSignalError() instead")
    void apiCommentsEntryTypeCommentsCommentIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsCommentIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsCommentIdPostSignalError() instead")
    void apiCommentsEntryTypeCommentsCommentIdPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsCommentIdPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsGetSignalError() instead")
    void apiCommentsEntryTypeCommentsGetSignalE(OAICommentForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsGetSignalError(OAICommentForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsPostSignalError() instead")
    void apiCommentsEntryTypeCommentsPostSignalE(OAICommentForApiContract summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsPostSignalError(OAICommentForApiContract summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsGetSignalError() instead")
    void apiCommentsGetSignalE(OAICommentForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsGetSignalError(OAICommentForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsCommentIdDeleteSignalErrorFull() instead")
    void apiCommentsEntryTypeCommentsCommentIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsCommentIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsCommentIdPostSignalErrorFull() instead")
    void apiCommentsEntryTypeCommentsCommentIdPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsCommentIdPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsGetSignalErrorFull() instead")
    void apiCommentsEntryTypeCommentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsEntryTypeCommentsPostSignalErrorFull() instead")
    void apiCommentsEntryTypeCommentsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsEntryTypeCommentsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiCommentsGetSignalErrorFull() instead")
    void apiCommentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiCommentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
