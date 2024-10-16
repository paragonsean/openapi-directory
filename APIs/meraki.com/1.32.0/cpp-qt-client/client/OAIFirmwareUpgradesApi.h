/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIFirmwareUpgradesApi_H
#define OAI_OAIFirmwareUpgradesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateNetworkFirmwareUpgradesRollback_200_response.h"
#include "OAICreateNetworkFirmwareUpgradesRollback_request.h"
#include "OAICreateNetworkFirmwareUpgradesStagedEvent_request.h"
#include "OAICreateNetworkFirmwareUpgradesStagedGroup_request.h"
#include "OAIGetNetworkFirmwareUpgradesStagedEvents_200_response.h"
#include "OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner.h"
#include "OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner.h"
#include "OAIGetNetworkFirmwareUpgrades_200_response.h"
#include "OAIObject.h"
#include "OAIRollbacksNetworkFirmwareUpgradesStagedEvents_request.h"
#include "OAIUpdateNetworkFirmwareUpgradesStagedEvents_request.h"
#include "OAIUpdateNetworkFirmwareUpgradesStagedStages_request.h"
#include "OAIUpdateNetworkFirmwareUpgrades_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIFirmwareUpgradesApi : public QObject {
    Q_OBJECT

public:
    OAIFirmwareUpgradesApi(const int timeOut = 0);
    ~OAIFirmwareUpgradesApi();

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
    * @param[in]  network_id QString [required]
    * @param[in]  oai_create_network_firmware_upgrades_rollback_request OAICreateNetworkFirmwareUpgradesRollback_request [required]
    */
    virtual void createNetworkFirmwareUpgradesRollback(const QString &network_id, const OAICreateNetworkFirmwareUpgradesRollback_request &oai_create_network_firmware_upgrades_rollback_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_create_network_firmware_upgrades_staged_event_request OAICreateNetworkFirmwareUpgradesStagedEvent_request [required]
    */
    virtual void createNetworkFirmwareUpgradesStagedEvent(const QString &network_id, const OAICreateNetworkFirmwareUpgradesStagedEvent_request &oai_create_network_firmware_upgrades_staged_event_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_create_network_firmware_upgrades_staged_group_request OAICreateNetworkFirmwareUpgradesStagedGroup_request [required]
    */
    virtual void createNetworkFirmwareUpgradesStagedGroup(const QString &network_id, const OAICreateNetworkFirmwareUpgradesStagedGroup_request &oai_create_network_firmware_upgrades_staged_group_request);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void deferNetworkFirmwareUpgradesStagedEvents(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  group_id QString [required]
    */
    virtual void deleteNetworkFirmwareUpgradesStagedGroup(const QString &network_id, const QString &group_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkFirmwareUpgradesStagedEvents(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  group_id QString [required]
    */
    virtual void getNetworkFirmwareUpgradesStagedGroup(const QString &network_id, const QString &group_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkFirmwareUpgradesStagedGroups(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkFirmwareUpgradesStagedStages(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkFirmwareUpgrades(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_rollbacks_network_firmware_upgrades_staged_events_request OAIRollbacksNetworkFirmwareUpgradesStagedEvents_request [required]
    */
    virtual void rollbacksNetworkFirmwareUpgradesStagedEvents(const QString &network_id, const OAIRollbacksNetworkFirmwareUpgradesStagedEvents_request &oai_rollbacks_network_firmware_upgrades_staged_events_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_firmware_upgrades_staged_events_request OAIUpdateNetworkFirmwareUpgradesStagedEvents_request [required]
    */
    virtual void updateNetworkFirmwareUpgradesStagedEvents(const QString &network_id, const OAIUpdateNetworkFirmwareUpgradesStagedEvents_request &oai_update_network_firmware_upgrades_staged_events_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  group_id QString [required]
    * @param[in]  oai_create_network_firmware_upgrades_staged_group_request OAICreateNetworkFirmwareUpgradesStagedGroup_request [required]
    */
    virtual void updateNetworkFirmwareUpgradesStagedGroup(const QString &network_id, const QString &group_id, const OAICreateNetworkFirmwareUpgradesStagedGroup_request &oai_create_network_firmware_upgrades_staged_group_request);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_firmware_upgrades_staged_stages_request OAIUpdateNetworkFirmwareUpgradesStagedStages_request [optional]
    */
    virtual void updateNetworkFirmwareUpgradesStagedStages(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkFirmwareUpgradesStagedStages_request> &oai_update_network_firmware_upgrades_staged_stages_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkFirmwareUpgradesStagedStages_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_firmware_upgrades_request OAIUpdateNetworkFirmwareUpgrades_request [optional]
    */
    virtual void updateNetworkFirmwareUpgrades(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkFirmwareUpgrades_request> &oai_update_network_firmware_upgrades_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkFirmwareUpgrades_request>());


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

    void createNetworkFirmwareUpgradesRollbackCallback(OAIHttpRequestWorker *worker);
    void createNetworkFirmwareUpgradesStagedEventCallback(OAIHttpRequestWorker *worker);
    void createNetworkFirmwareUpgradesStagedGroupCallback(OAIHttpRequestWorker *worker);
    void deferNetworkFirmwareUpgradesStagedEventsCallback(OAIHttpRequestWorker *worker);
    void deleteNetworkFirmwareUpgradesStagedGroupCallback(OAIHttpRequestWorker *worker);
    void getNetworkFirmwareUpgradesStagedEventsCallback(OAIHttpRequestWorker *worker);
    void getNetworkFirmwareUpgradesStagedGroupCallback(OAIHttpRequestWorker *worker);
    void getNetworkFirmwareUpgradesStagedGroupsCallback(OAIHttpRequestWorker *worker);
    void getNetworkFirmwareUpgradesStagedStagesCallback(OAIHttpRequestWorker *worker);
    void getNetworkFirmwareUpgradesCallback(OAIHttpRequestWorker *worker);
    void rollbacksNetworkFirmwareUpgradesStagedEventsCallback(OAIHttpRequestWorker *worker);
    void updateNetworkFirmwareUpgradesStagedEventsCallback(OAIHttpRequestWorker *worker);
    void updateNetworkFirmwareUpgradesStagedGroupCallback(OAIHttpRequestWorker *worker);
    void updateNetworkFirmwareUpgradesStagedStagesCallback(OAIHttpRequestWorker *worker);
    void updateNetworkFirmwareUpgradesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createNetworkFirmwareUpgradesRollbackSignal(OAICreateNetworkFirmwareUpgradesRollback_200_response summary);
    void createNetworkFirmwareUpgradesStagedEventSignal(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void createNetworkFirmwareUpgradesStagedGroupSignal(OAIObject summary);
    void deferNetworkFirmwareUpgradesStagedEventsSignal(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void deleteNetworkFirmwareUpgradesStagedGroupSignal();
    void getNetworkFirmwareUpgradesStagedEventsSignal(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void getNetworkFirmwareUpgradesStagedGroupSignal(OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner summary);
    void getNetworkFirmwareUpgradesStagedGroupsSignal(QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner> summary);
    void getNetworkFirmwareUpgradesStagedStagesSignal(QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary);
    void getNetworkFirmwareUpgradesSignal(OAIGetNetworkFirmwareUpgrades_200_response summary);
    void rollbacksNetworkFirmwareUpgradesStagedEventsSignal(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void updateNetworkFirmwareUpgradesStagedEventsSignal(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void updateNetworkFirmwareUpgradesStagedGroupSignal(OAIObject summary);
    void updateNetworkFirmwareUpgradesStagedStagesSignal(QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary);
    void updateNetworkFirmwareUpgradesSignal(OAIGetNetworkFirmwareUpgrades_200_response summary);


    void createNetworkFirmwareUpgradesRollbackSignalFull(OAIHttpRequestWorker *worker, OAICreateNetworkFirmwareUpgradesRollback_200_response summary);
    void createNetworkFirmwareUpgradesStagedEventSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void createNetworkFirmwareUpgradesStagedGroupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void deferNetworkFirmwareUpgradesStagedEventsSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void deleteNetworkFirmwareUpgradesStagedGroupSignalFull(OAIHttpRequestWorker *worker);
    void getNetworkFirmwareUpgradesStagedEventsSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void getNetworkFirmwareUpgradesStagedGroupSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner summary);
    void getNetworkFirmwareUpgradesStagedGroupsSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner> summary);
    void getNetworkFirmwareUpgradesStagedStagesSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary);
    void getNetworkFirmwareUpgradesSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgrades_200_response summary);
    void rollbacksNetworkFirmwareUpgradesStagedEventsSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void updateNetworkFirmwareUpgradesStagedEventsSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary);
    void updateNetworkFirmwareUpgradesStagedGroupSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateNetworkFirmwareUpgradesStagedStagesSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary);
    void updateNetworkFirmwareUpgradesSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkFirmwareUpgrades_200_response summary);

    Q_DECL_DEPRECATED_X("Use createNetworkFirmwareUpgradesRollbackSignalError() instead")
    void createNetworkFirmwareUpgradesRollbackSignalE(OAICreateNetworkFirmwareUpgradesRollback_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkFirmwareUpgradesRollbackSignalError(OAICreateNetworkFirmwareUpgradesRollback_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkFirmwareUpgradesStagedEventSignalError() instead")
    void createNetworkFirmwareUpgradesStagedEventSignalE(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkFirmwareUpgradesStagedEventSignalError(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkFirmwareUpgradesStagedGroupSignalError() instead")
    void createNetworkFirmwareUpgradesStagedGroupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkFirmwareUpgradesStagedGroupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deferNetworkFirmwareUpgradesStagedEventsSignalError() instead")
    void deferNetworkFirmwareUpgradesStagedEventsSignalE(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deferNetworkFirmwareUpgradesStagedEventsSignalError(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteNetworkFirmwareUpgradesStagedGroupSignalError() instead")
    void deleteNetworkFirmwareUpgradesStagedGroupSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteNetworkFirmwareUpgradesStagedGroupSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedEventsSignalError() instead")
    void getNetworkFirmwareUpgradesStagedEventsSignalE(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedEventsSignalError(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedGroupSignalError() instead")
    void getNetworkFirmwareUpgradesStagedGroupSignalE(OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedGroupSignalError(OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedGroupsSignalError() instead")
    void getNetworkFirmwareUpgradesStagedGroupsSignalE(QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedGroupsSignalError(QList<OAIGetNetworkFirmwareUpgradesStagedGroups_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedStagesSignalError() instead")
    void getNetworkFirmwareUpgradesStagedStagesSignalE(QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedStagesSignalError(QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesSignalError() instead")
    void getNetworkFirmwareUpgradesSignalE(OAIGetNetworkFirmwareUpgrades_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesSignalError(OAIGetNetworkFirmwareUpgrades_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rollbacksNetworkFirmwareUpgradesStagedEventsSignalError() instead")
    void rollbacksNetworkFirmwareUpgradesStagedEventsSignalE(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rollbacksNetworkFirmwareUpgradesStagedEventsSignalError(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesStagedEventsSignalError() instead")
    void updateNetworkFirmwareUpgradesStagedEventsSignalE(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesStagedEventsSignalError(OAIGetNetworkFirmwareUpgradesStagedEvents_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesStagedGroupSignalError() instead")
    void updateNetworkFirmwareUpgradesStagedGroupSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesStagedGroupSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesStagedStagesSignalError() instead")
    void updateNetworkFirmwareUpgradesStagedStagesSignalE(QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesStagedStagesSignalError(QList<OAIGetNetworkFirmwareUpgradesStagedStages_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesSignalError() instead")
    void updateNetworkFirmwareUpgradesSignalE(OAIGetNetworkFirmwareUpgrades_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesSignalError(OAIGetNetworkFirmwareUpgrades_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createNetworkFirmwareUpgradesRollbackSignalErrorFull() instead")
    void createNetworkFirmwareUpgradesRollbackSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkFirmwareUpgradesRollbackSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkFirmwareUpgradesStagedEventSignalErrorFull() instead")
    void createNetworkFirmwareUpgradesStagedEventSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkFirmwareUpgradesStagedEventSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createNetworkFirmwareUpgradesStagedGroupSignalErrorFull() instead")
    void createNetworkFirmwareUpgradesStagedGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createNetworkFirmwareUpgradesStagedGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deferNetworkFirmwareUpgradesStagedEventsSignalErrorFull() instead")
    void deferNetworkFirmwareUpgradesStagedEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deferNetworkFirmwareUpgradesStagedEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteNetworkFirmwareUpgradesStagedGroupSignalErrorFull() instead")
    void deleteNetworkFirmwareUpgradesStagedGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteNetworkFirmwareUpgradesStagedGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedEventsSignalErrorFull() instead")
    void getNetworkFirmwareUpgradesStagedEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedGroupSignalErrorFull() instead")
    void getNetworkFirmwareUpgradesStagedGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedGroupsSignalErrorFull() instead")
    void getNetworkFirmwareUpgradesStagedGroupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedGroupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesStagedStagesSignalErrorFull() instead")
    void getNetworkFirmwareUpgradesStagedStagesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesStagedStagesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkFirmwareUpgradesSignalErrorFull() instead")
    void getNetworkFirmwareUpgradesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkFirmwareUpgradesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rollbacksNetworkFirmwareUpgradesStagedEventsSignalErrorFull() instead")
    void rollbacksNetworkFirmwareUpgradesStagedEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rollbacksNetworkFirmwareUpgradesStagedEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesStagedEventsSignalErrorFull() instead")
    void updateNetworkFirmwareUpgradesStagedEventsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesStagedEventsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesStagedGroupSignalErrorFull() instead")
    void updateNetworkFirmwareUpgradesStagedGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesStagedGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesStagedStagesSignalErrorFull() instead")
    void updateNetworkFirmwareUpgradesStagedStagesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesStagedStagesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkFirmwareUpgradesSignalErrorFull() instead")
    void updateNetworkFirmwareUpgradesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkFirmwareUpgradesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
