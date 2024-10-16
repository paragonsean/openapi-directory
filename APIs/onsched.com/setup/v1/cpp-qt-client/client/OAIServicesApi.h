/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIServicesApi_H
#define OAI_OAIServicesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAvailabilityInputModel.h"
#include "OAIResourceBlockViewModel.h"
#include "OAIResourceListViewModel.h"
#include "OAIServiceAllocationInputModel.h"
#include "OAIServiceAllocationListViewModel.h"
#include "OAIServiceAllocationUpdateModel.h"
#include "OAIServiceAllocationViewModel.h"
#include "OAIServiceAllocationsInputModel.h"
#include "OAIServiceAvailabilityViewModel.h"
#include "OAIServiceBlockInputModel.h"
#include "OAIServiceBlockListViewModel.h"
#include "OAIServiceBlockUpdateModel.h"
#include "OAIServiceBlockViewModel.h"
#include "OAIServiceCalendarInputModel.h"
#include "OAIServiceCalendarViewModel.h"
#include "OAIServiceImageInputModel.h"
#include "OAIServiceInputModel.h"
#include "OAIServiceListViewModel.h"
#include "OAIServiceUpdateModel.h"
#include "OAIServiceViewModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIServicesApi : public QObject {
    Q_OBJECT

public:
    OAIServicesApi(const int timeOut = 0);
    ~OAIServicesApi();

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
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesAllocationsIdDelete(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesAllocationsIdGet(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_service_allocation_update_model OAIServiceAllocationUpdateModel [optional]
    */
    virtual void setupV1ServicesAllocationsIdPut(const QString &id, const ::OpenAPI::OptionalParam<OAIServiceAllocationUpdateModel> &oai_service_allocation_update_model = ::OpenAPI::OptionalParam<OAIServiceAllocationUpdateModel>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesBlockIdDelete(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_service_block_update_model OAIServiceBlockUpdateModel [optional]
    */
    virtual void setupV1ServicesBlockIdPut(const QString &id, const ::OpenAPI::OptionalParam<OAIServiceBlockUpdateModel> &oai_service_block_update_model = ::OpenAPI::OptionalParam<OAIServiceBlockUpdateModel>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesBlocksIdGet(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesCalendarIdDelete(const QString &id);

    /**
    * @param[in]  oai_service_calendar_input_model OAIServiceCalendarInputModel [optional]
    */
    virtual void setupV1ServicesCalendarPost(const ::OpenAPI::OptionalParam<OAIServiceCalendarInputModel> &oai_service_calendar_input_model = ::OpenAPI::OptionalParam<OAIServiceCalendarInputModel>());

    /**
    * @param[in]  location_id QString [optional]
    * @param[in]  service_group_id qint32 [optional]
    * @param[in]  deleted bool [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void setupV1ServicesGet(const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &service_group_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &deleted = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_service_allocations_input_model OAIServiceAllocationsInputModel [optional]
    */
    virtual void setupV1ServicesIdAllocationsBulkPost(const QString &id, const ::OpenAPI::OptionalParam<OAIServiceAllocationsInputModel> &oai_service_allocations_input_model = ::OpenAPI::OptionalParam<OAIServiceAllocationsInputModel>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  location_id QString [optional]
    * @param[in]  resource_id QString [optional]
    * @param[in]  start_date QDateTime [optional]
    * @param[in]  end_date QDateTime [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void setupV1ServicesIdAllocationsGet(const QString &id, const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &resource_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &start_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_service_allocation_input_model OAIServiceAllocationInputModel [optional]
    */
    virtual void setupV1ServicesIdAllocationsPost(const QString &id, const ::OpenAPI::OptionalParam<OAIServiceAllocationInputModel> &oai_service_allocation_input_model = ::OpenAPI::OptionalParam<OAIServiceAllocationInputModel>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesIdAvailabilityGet(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_availability_input_model OAIAvailabilityInputModel [optional]
    */
    virtual void setupV1ServicesIdAvailabilityPut(const QString &id, const ::OpenAPI::OptionalParam<OAIAvailabilityInputModel> &oai_availability_input_model = ::OpenAPI::OptionalParam<OAIAvailabilityInputModel>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_service_block_input_model OAIServiceBlockInputModel [optional]
    */
    virtual void setupV1ServicesIdBlockPost(const QString &id, const ::OpenAPI::OptionalParam<OAIServiceBlockInputModel> &oai_service_block_input_model = ::OpenAPI::OptionalParam<OAIServiceBlockInputModel>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  start_date QDateTime [optional]
    * @param[in]  end_date QDateTime [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void setupV1ServicesIdBlocksGet(const QString &id, const ::OpenAPI::OptionalParam<QDateTime> &start_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &end_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  location_id QString [optional]
    */
    virtual void setupV1ServicesIdCalendarGet(const QString &id, const ::OpenAPI::OptionalParam<QString> &location_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesIdDelete(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesIdDeleteimageDelete(const QString &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void setupV1ServicesIdGet(const qint32 &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_service_update_model OAIServiceUpdateModel [optional]
    */
    virtual void setupV1ServicesIdPut(const QString &id, const ::OpenAPI::OptionalParam<OAIServiceUpdateModel> &oai_service_update_model = ::OpenAPI::OptionalParam<OAIServiceUpdateModel>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupV1ServicesIdRecoverPut(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  google_auth_return_url QString [optional]
    * @param[in]  outlook_auth_return_url QString [optional]
    */
    virtual void setupV1ServicesIdResourcesGet(const QString &id, const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &google_auth_return_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &outlook_auth_return_url = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_service_image_input_model OAIServiceImageInputModel [optional]
    */
    virtual void setupV1ServicesIdUploadimagePost(const QString &id, const ::OpenAPI::OptionalParam<OAIServiceImageInputModel> &oai_service_image_input_model = ::OpenAPI::OptionalParam<OAIServiceImageInputModel>());

    /**
    * @param[in]  oai_service_input_model OAIServiceInputModel [optional]
    */
    virtual void setupV1ServicesPost(const ::OpenAPI::OptionalParam<OAIServiceInputModel> &oai_service_input_model = ::OpenAPI::OptionalParam<OAIServiceInputModel>());


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

    void setupV1ServicesAllocationsIdDeleteCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesAllocationsIdGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesAllocationsIdPutCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesBlockIdDeleteCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesBlockIdPutCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesBlocksIdGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesCalendarIdDeleteCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesCalendarPostCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdAllocationsBulkPostCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdAllocationsGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdAllocationsPostCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdAvailabilityGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdAvailabilityPutCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdBlockPostCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdBlocksGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdCalendarGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdDeleteCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdDeleteimageDeleteCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdPutCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdRecoverPutCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdResourcesGetCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesIdUploadimagePostCallback(OAIHttpRequestWorker *worker);
    void setupV1ServicesPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void setupV1ServicesAllocationsIdDeleteSignal(OAIServiceAllocationViewModel summary);
    void setupV1ServicesAllocationsIdGetSignal(OAIServiceAllocationViewModel summary);
    void setupV1ServicesAllocationsIdPutSignal(OAIServiceAllocationViewModel summary);
    void setupV1ServicesBlockIdDeleteSignal(OAIResourceBlockViewModel summary);
    void setupV1ServicesBlockIdPutSignal(OAIServiceBlockViewModel summary);
    void setupV1ServicesBlocksIdGetSignal(OAIResourceBlockViewModel summary);
    void setupV1ServicesCalendarIdDeleteSignal(OAIServiceCalendarViewModel summary);
    void setupV1ServicesCalendarPostSignal(OAIServiceCalendarViewModel summary);
    void setupV1ServicesGetSignal(OAIServiceListViewModel summary);
    void setupV1ServicesIdAllocationsBulkPostSignal(QList<OAIServiceAllocationViewModel> summary);
    void setupV1ServicesIdAllocationsGetSignal(OAIServiceAllocationListViewModel summary);
    void setupV1ServicesIdAllocationsPostSignal(OAIServiceAllocationViewModel summary);
    void setupV1ServicesIdAvailabilityGetSignal(OAIServiceAvailabilityViewModel summary);
    void setupV1ServicesIdAvailabilityPutSignal(OAIServiceAvailabilityViewModel summary);
    void setupV1ServicesIdBlockPostSignal(OAIServiceBlockViewModel summary);
    void setupV1ServicesIdBlocksGetSignal(OAIServiceBlockListViewModel summary);
    void setupV1ServicesIdCalendarGetSignal(OAIServiceCalendarViewModel summary);
    void setupV1ServicesIdDeleteSignal(OAIServiceViewModel summary);
    void setupV1ServicesIdDeleteimageDeleteSignal(OAIServiceViewModel summary);
    void setupV1ServicesIdGetSignal(OAIServiceViewModel summary);
    void setupV1ServicesIdPutSignal(OAIServiceViewModel summary);
    void setupV1ServicesIdRecoverPutSignal(OAIServiceViewModel summary);
    void setupV1ServicesIdResourcesGetSignal(OAIResourceListViewModel summary);
    void setupV1ServicesIdUploadimagePostSignal(OAIServiceViewModel summary);
    void setupV1ServicesPostSignal(OAIServiceViewModel summary);


    void setupV1ServicesAllocationsIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIServiceAllocationViewModel summary);
    void setupV1ServicesAllocationsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceAllocationViewModel summary);
    void setupV1ServicesAllocationsIdPutSignalFull(OAIHttpRequestWorker *worker, OAIServiceAllocationViewModel summary);
    void setupV1ServicesBlockIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIResourceBlockViewModel summary);
    void setupV1ServicesBlockIdPutSignalFull(OAIHttpRequestWorker *worker, OAIServiceBlockViewModel summary);
    void setupV1ServicesBlocksIdGetSignalFull(OAIHttpRequestWorker *worker, OAIResourceBlockViewModel summary);
    void setupV1ServicesCalendarIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIServiceCalendarViewModel summary);
    void setupV1ServicesCalendarPostSignalFull(OAIHttpRequestWorker *worker, OAIServiceCalendarViewModel summary);
    void setupV1ServicesGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceListViewModel summary);
    void setupV1ServicesIdAllocationsBulkPostSignalFull(OAIHttpRequestWorker *worker, QList<OAIServiceAllocationViewModel> summary);
    void setupV1ServicesIdAllocationsGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceAllocationListViewModel summary);
    void setupV1ServicesIdAllocationsPostSignalFull(OAIHttpRequestWorker *worker, OAIServiceAllocationViewModel summary);
    void setupV1ServicesIdAvailabilityGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceAvailabilityViewModel summary);
    void setupV1ServicesIdAvailabilityPutSignalFull(OAIHttpRequestWorker *worker, OAIServiceAvailabilityViewModel summary);
    void setupV1ServicesIdBlockPostSignalFull(OAIHttpRequestWorker *worker, OAIServiceBlockViewModel summary);
    void setupV1ServicesIdBlocksGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceBlockListViewModel summary);
    void setupV1ServicesIdCalendarGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceCalendarViewModel summary);
    void setupV1ServicesIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);
    void setupV1ServicesIdDeleteimageDeleteSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);
    void setupV1ServicesIdGetSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);
    void setupV1ServicesIdPutSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);
    void setupV1ServicesIdRecoverPutSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);
    void setupV1ServicesIdResourcesGetSignalFull(OAIHttpRequestWorker *worker, OAIResourceListViewModel summary);
    void setupV1ServicesIdUploadimagePostSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);
    void setupV1ServicesPostSignalFull(OAIHttpRequestWorker *worker, OAIServiceViewModel summary);

    Q_DECL_DEPRECATED_X("Use setupV1ServicesAllocationsIdDeleteSignalError() instead")
    void setupV1ServicesAllocationsIdDeleteSignalE(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesAllocationsIdDeleteSignalError(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesAllocationsIdGetSignalError() instead")
    void setupV1ServicesAllocationsIdGetSignalE(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesAllocationsIdGetSignalError(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesAllocationsIdPutSignalError() instead")
    void setupV1ServicesAllocationsIdPutSignalE(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesAllocationsIdPutSignalError(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesBlockIdDeleteSignalError() instead")
    void setupV1ServicesBlockIdDeleteSignalE(OAIResourceBlockViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesBlockIdDeleteSignalError(OAIResourceBlockViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesBlockIdPutSignalError() instead")
    void setupV1ServicesBlockIdPutSignalE(OAIServiceBlockViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesBlockIdPutSignalError(OAIServiceBlockViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesBlocksIdGetSignalError() instead")
    void setupV1ServicesBlocksIdGetSignalE(OAIResourceBlockViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesBlocksIdGetSignalError(OAIResourceBlockViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesCalendarIdDeleteSignalError() instead")
    void setupV1ServicesCalendarIdDeleteSignalE(OAIServiceCalendarViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesCalendarIdDeleteSignalError(OAIServiceCalendarViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesCalendarPostSignalError() instead")
    void setupV1ServicesCalendarPostSignalE(OAIServiceCalendarViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesCalendarPostSignalError(OAIServiceCalendarViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesGetSignalError() instead")
    void setupV1ServicesGetSignalE(OAIServiceListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesGetSignalError(OAIServiceListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAllocationsBulkPostSignalError() instead")
    void setupV1ServicesIdAllocationsBulkPostSignalE(QList<OAIServiceAllocationViewModel> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAllocationsBulkPostSignalError(QList<OAIServiceAllocationViewModel> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAllocationsGetSignalError() instead")
    void setupV1ServicesIdAllocationsGetSignalE(OAIServiceAllocationListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAllocationsGetSignalError(OAIServiceAllocationListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAllocationsPostSignalError() instead")
    void setupV1ServicesIdAllocationsPostSignalE(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAllocationsPostSignalError(OAIServiceAllocationViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAvailabilityGetSignalError() instead")
    void setupV1ServicesIdAvailabilityGetSignalE(OAIServiceAvailabilityViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAvailabilityGetSignalError(OAIServiceAvailabilityViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAvailabilityPutSignalError() instead")
    void setupV1ServicesIdAvailabilityPutSignalE(OAIServiceAvailabilityViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAvailabilityPutSignalError(OAIServiceAvailabilityViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdBlockPostSignalError() instead")
    void setupV1ServicesIdBlockPostSignalE(OAIServiceBlockViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdBlockPostSignalError(OAIServiceBlockViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdBlocksGetSignalError() instead")
    void setupV1ServicesIdBlocksGetSignalE(OAIServiceBlockListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdBlocksGetSignalError(OAIServiceBlockListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdCalendarGetSignalError() instead")
    void setupV1ServicesIdCalendarGetSignalE(OAIServiceCalendarViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdCalendarGetSignalError(OAIServiceCalendarViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdDeleteSignalError() instead")
    void setupV1ServicesIdDeleteSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdDeleteSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdDeleteimageDeleteSignalError() instead")
    void setupV1ServicesIdDeleteimageDeleteSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdDeleteimageDeleteSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdGetSignalError() instead")
    void setupV1ServicesIdGetSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdGetSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdPutSignalError() instead")
    void setupV1ServicesIdPutSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdPutSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdRecoverPutSignalError() instead")
    void setupV1ServicesIdRecoverPutSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdRecoverPutSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdResourcesGetSignalError() instead")
    void setupV1ServicesIdResourcesGetSignalE(OAIResourceListViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdResourcesGetSignalError(OAIResourceListViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdUploadimagePostSignalError() instead")
    void setupV1ServicesIdUploadimagePostSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdUploadimagePostSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesPostSignalError() instead")
    void setupV1ServicesPostSignalE(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesPostSignalError(OAIServiceViewModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use setupV1ServicesAllocationsIdDeleteSignalErrorFull() instead")
    void setupV1ServicesAllocationsIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesAllocationsIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesAllocationsIdGetSignalErrorFull() instead")
    void setupV1ServicesAllocationsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesAllocationsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesAllocationsIdPutSignalErrorFull() instead")
    void setupV1ServicesAllocationsIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesAllocationsIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesBlockIdDeleteSignalErrorFull() instead")
    void setupV1ServicesBlockIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesBlockIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesBlockIdPutSignalErrorFull() instead")
    void setupV1ServicesBlockIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesBlockIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesBlocksIdGetSignalErrorFull() instead")
    void setupV1ServicesBlocksIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesBlocksIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesCalendarIdDeleteSignalErrorFull() instead")
    void setupV1ServicesCalendarIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesCalendarIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesCalendarPostSignalErrorFull() instead")
    void setupV1ServicesCalendarPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesCalendarPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesGetSignalErrorFull() instead")
    void setupV1ServicesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAllocationsBulkPostSignalErrorFull() instead")
    void setupV1ServicesIdAllocationsBulkPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAllocationsBulkPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAllocationsGetSignalErrorFull() instead")
    void setupV1ServicesIdAllocationsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAllocationsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAllocationsPostSignalErrorFull() instead")
    void setupV1ServicesIdAllocationsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAllocationsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAvailabilityGetSignalErrorFull() instead")
    void setupV1ServicesIdAvailabilityGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAvailabilityGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdAvailabilityPutSignalErrorFull() instead")
    void setupV1ServicesIdAvailabilityPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdAvailabilityPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdBlockPostSignalErrorFull() instead")
    void setupV1ServicesIdBlockPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdBlockPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdBlocksGetSignalErrorFull() instead")
    void setupV1ServicesIdBlocksGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdBlocksGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdCalendarGetSignalErrorFull() instead")
    void setupV1ServicesIdCalendarGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdCalendarGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdDeleteSignalErrorFull() instead")
    void setupV1ServicesIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdDeleteimageDeleteSignalErrorFull() instead")
    void setupV1ServicesIdDeleteimageDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdDeleteimageDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdGetSignalErrorFull() instead")
    void setupV1ServicesIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdPutSignalErrorFull() instead")
    void setupV1ServicesIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdRecoverPutSignalErrorFull() instead")
    void setupV1ServicesIdRecoverPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdRecoverPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdResourcesGetSignalErrorFull() instead")
    void setupV1ServicesIdResourcesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdResourcesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesIdUploadimagePostSignalErrorFull() instead")
    void setupV1ServicesIdUploadimagePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesIdUploadimagePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupV1ServicesPostSignalErrorFull() instead")
    void setupV1ServicesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupV1ServicesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
