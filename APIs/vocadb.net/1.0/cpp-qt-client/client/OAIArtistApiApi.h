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

#ifndef OAI_OAIArtistApiApi_H
#define OAI_OAIArtistApiApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAdvancedSearchFilterParams.h"
#include "OAIArtistForApiContract.h"
#include "OAIArtistForApiContractPartialFindResult.h"
#include "OAIArtistOptionalFields.h"
#include "OAIArtistRelationsFields.h"
#include "OAIArtistSortRule.h"
#include "OAICommentForApiContract.h"
#include "OAIContentLanguagePreference.h"
#include "OAIEntryStatus.h"
#include "OAINameMatchMode.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIArtistApiApi : public QObject {
    Q_OBJECT

public:
    OAIArtistApiApi(const int timeOut = 0);
    ~OAIArtistApiApi();

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
    * @param[in]  comment_id qint32 [required]
    */
    virtual void apiArtistsCommentsCommentIdDelete(const qint32 &comment_id);

    /**
    * @param[in]  comment_id qint32 [required]
    * @param[in]  oai_comment_for_api_contract OAICommentForApiContract [optional]
    */
    virtual void apiArtistsCommentsCommentIdPost(const qint32 &comment_id, const ::OpenAPI::OptionalParam<OAICommentForApiContract> &oai_comment_for_api_contract = ::OpenAPI::OptionalParam<OAICommentForApiContract>());

    /**
    * @param[in]  query QString [optional]
    * @param[in]  artist_types QString [optional]
    * @param[in]  allow_base_voicebanks bool [optional]
    * @param[in]  tag_name QList<QString> [optional]
    * @param[in]  tag_id QList<qint32> [optional]
    * @param[in]  child_tags bool [optional]
    * @param[in]  followed_by_user_id qint32 [optional]
    * @param[in]  status OAIEntryStatus [optional]
    * @param[in]  advanced_filters QList<OAIAdvancedSearchFilterParams> [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  max_results qint32 [optional]
    * @param[in]  get_total_count bool [optional]
    * @param[in]  sort OAIArtistSortRule [optional]
    * @param[in]  prefer_accurate_matches bool [optional]
    * @param[in]  name_match_mode OAINameMatchMode [optional]
    * @param[in]  fields OAIArtistOptionalFields [optional]
    * @param[in]  lang OAIContentLanguagePreference [optional]
    */
    virtual void apiArtistsGet(const ::OpenAPI::OptionalParam<QString> &query = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &artist_types = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &allow_base_voicebanks = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QList<QString>> &tag_name = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QList<qint32>> &tag_id = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<bool> &child_tags = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &followed_by_user_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIEntryStatus> &status = ::OpenAPI::OptionalParam<OAIEntryStatus>(), const ::OpenAPI::OptionalParam<QList<OAIAdvancedSearchFilterParams>> &advanced_filters = ::OpenAPI::OptionalParam<QList<OAIAdvancedSearchFilterParams>>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &get_total_count = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAIArtistSortRule> &sort = ::OpenAPI::OptionalParam<OAIArtistSortRule>(), const ::OpenAPI::OptionalParam<bool> &prefer_accurate_matches = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAINameMatchMode> &name_match_mode = ::OpenAPI::OptionalParam<OAINameMatchMode>(), const ::OpenAPI::OptionalParam<OAIArtistOptionalFields> &fields = ::OpenAPI::OptionalParam<OAIArtistOptionalFields>(), const ::OpenAPI::OptionalParam<OAIContentLanguagePreference> &lang = ::OpenAPI::OptionalParam<OAIContentLanguagePreference>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void apiArtistsIdCommentsGet(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_comment_for_api_contract OAICommentForApiContract [optional]
    */
    virtual void apiArtistsIdCommentsPost(const qint32 &id, const ::OpenAPI::OptionalParam<OAICommentForApiContract> &oai_comment_for_api_contract = ::OpenAPI::OptionalParam<OAICommentForApiContract>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  notes QString [optional]
    */
    virtual void apiArtistsIdDelete(const qint32 &id, const ::OpenAPI::OptionalParam<QString> &notes = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  fields OAIArtistOptionalFields [optional]
    * @param[in]  relations OAIArtistRelationsFields [optional]
    * @param[in]  lang OAIContentLanguagePreference [optional]
    */
    virtual void apiArtistsIdGet(const qint32 &id, const ::OpenAPI::OptionalParam<OAIArtistOptionalFields> &fields = ::OpenAPI::OptionalParam<OAIArtistOptionalFields>(), const ::OpenAPI::OptionalParam<OAIArtistRelationsFields> &relations = ::OpenAPI::OptionalParam<OAIArtistRelationsFields>(), const ::OpenAPI::OptionalParam<OAIContentLanguagePreference> &lang = ::OpenAPI::OptionalParam<OAIContentLanguagePreference>());

    /**
    * @param[in]  query QString [optional]
    * @param[in]  name_match_mode OAINameMatchMode [optional]
    * @param[in]  max_results qint32 [optional]
    */
    virtual void apiArtistsNamesGet(const ::OpenAPI::OptionalParam<QString> &query = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAINameMatchMode> &name_match_mode = ::OpenAPI::OptionalParam<OAINameMatchMode>(), const ::OpenAPI::OptionalParam<qint32> &max_results = ::OpenAPI::OptionalParam<qint32>());


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

    void apiArtistsCommentsCommentIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiArtistsCommentsCommentIdPostCallback(OAIHttpRequestWorker *worker);
    void apiArtistsGetCallback(OAIHttpRequestWorker *worker);
    void apiArtistsIdCommentsGetCallback(OAIHttpRequestWorker *worker);
    void apiArtistsIdCommentsPostCallback(OAIHttpRequestWorker *worker);
    void apiArtistsIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiArtistsIdGetCallback(OAIHttpRequestWorker *worker);
    void apiArtistsNamesGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiArtistsCommentsCommentIdDeleteSignal();
    void apiArtistsCommentsCommentIdPostSignal();
    void apiArtistsGetSignal(OAIArtistForApiContractPartialFindResult summary);
    void apiArtistsIdCommentsGetSignal(QList<OAICommentForApiContract> summary);
    void apiArtistsIdCommentsPostSignal(OAICommentForApiContract summary);
    void apiArtistsIdDeleteSignal();
    void apiArtistsIdGetSignal(OAIArtistForApiContract summary);
    void apiArtistsNamesGetSignal(QList<QString> summary);


    void apiArtistsCommentsCommentIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiArtistsCommentsCommentIdPostSignalFull(OAIHttpRequestWorker *worker);
    void apiArtistsGetSignalFull(OAIHttpRequestWorker *worker, OAIArtistForApiContractPartialFindResult summary);
    void apiArtistsIdCommentsGetSignalFull(OAIHttpRequestWorker *worker, QList<OAICommentForApiContract> summary);
    void apiArtistsIdCommentsPostSignalFull(OAIHttpRequestWorker *worker, OAICommentForApiContract summary);
    void apiArtistsIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiArtistsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIArtistForApiContract summary);
    void apiArtistsNamesGetSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);

    Q_DECL_DEPRECATED_X("Use apiArtistsCommentsCommentIdDeleteSignalError() instead")
    void apiArtistsCommentsCommentIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsCommentsCommentIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsCommentsCommentIdPostSignalError() instead")
    void apiArtistsCommentsCommentIdPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsCommentsCommentIdPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsGetSignalError() instead")
    void apiArtistsGetSignalE(OAIArtistForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsGetSignalError(OAIArtistForApiContractPartialFindResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdCommentsGetSignalError() instead")
    void apiArtistsIdCommentsGetSignalE(QList<OAICommentForApiContract> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdCommentsGetSignalError(QList<OAICommentForApiContract> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdCommentsPostSignalError() instead")
    void apiArtistsIdCommentsPostSignalE(OAICommentForApiContract summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdCommentsPostSignalError(OAICommentForApiContract summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdDeleteSignalError() instead")
    void apiArtistsIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdGetSignalError() instead")
    void apiArtistsIdGetSignalE(OAIArtistForApiContract summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdGetSignalError(OAIArtistForApiContract summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsNamesGetSignalError() instead")
    void apiArtistsNamesGetSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsNamesGetSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiArtistsCommentsCommentIdDeleteSignalErrorFull() instead")
    void apiArtistsCommentsCommentIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsCommentsCommentIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsCommentsCommentIdPostSignalErrorFull() instead")
    void apiArtistsCommentsCommentIdPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsCommentsCommentIdPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsGetSignalErrorFull() instead")
    void apiArtistsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdCommentsGetSignalErrorFull() instead")
    void apiArtistsIdCommentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdCommentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdCommentsPostSignalErrorFull() instead")
    void apiArtistsIdCommentsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdCommentsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdDeleteSignalErrorFull() instead")
    void apiArtistsIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsIdGetSignalErrorFull() instead")
    void apiArtistsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiArtistsNamesGetSignalErrorFull() instead")
    void apiArtistsNamesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiArtistsNamesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
