/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAbsencePeriodsResponse.h"
#include "OAIAttendancePeriodsResponse.h"
#include "OAICreateTimeOffPeriodRequest.h"
#include "OAIDetailedErrorResponse.h"
#include "OAIEmployeeResponse.h"
#include "OAIEmployeesResponse.h"
#include "OAIErrorResponse.h"
#include "OAIHttpFileElement.h"
#include "OAINewAttendancePeriodRequest.h"
#include "OAINewAttendancePeriodResponse.h"
#include "OAIObject.h"
#include "OAIResponse.h"
#include "OAIUpdateAttendancePeriodRequest.h"
#include "OAI_company_time_off_types_get_200_response.h"
#include "OAI_company_time_offs_post_201_response.h"
#include <QString>
#include <QDate>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

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
    * @param[in]  start_date QDate [required]
    * @param[in]  end_date QDate [required]
    * @param[in]  updated_from QString [optional]
    * @param[in]  updated_to QString [optional]
    * @param[in]  employees QList<qint32> [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void companyAttendancesGet(const QDate &start_date, const QDate &end_date, const ::OpenAPI::OptionalParam<QString> &updated_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &updated_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<qint32>> &employees = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void companyAttendancesIdDelete(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_update_attendance_period_request OAIUpdateAttendancePeriodRequest [required]
    */
    virtual void companyAttendancesIdPatch(const qint32 &id, const OAIUpdateAttendancePeriodRequest &oai_update_attendance_period_request);

    /**
    * @param[in]  oai_new_attendance_period_request OAINewAttendancePeriodRequest [required]
    */
    virtual void companyAttendancesPost(const OAINewAttendancePeriodRequest &oai_new_attendance_period_request);

    /**
    * @param[in]  employee_id qint32 [required]
    */
    virtual void companyEmployeesEmployeeIdGet(const qint32 &employee_id);

    /**
    * @param[in]  employee_id qint32 [required]
    * @param[in]  width qint32 [required]
    */
    virtual void companyEmployeesEmployeeIdProfilePictureWidthGet(const qint32 &employee_id, const qint32 &width);


    virtual void companyEmployeesGet();

    /**
    * @param[in]  employee_email QString [required]
    * @param[in]  employee_first_name QString [required]
    * @param[in]  employee_last_name QString [required]
    * @param[in]  employee_department QString [optional]
    * @param[in]  employee_gender QString [optional]
    * @param[in]  employee_hire_date QDate [optional]
    * @param[in]  employee_position QString [optional]
    * @param[in]  employee_weekly_hours double [optional]
    */
    virtual void companyEmployeesPost(const QString &employee_email, const QString &employee_first_name, const QString &employee_last_name, const ::OpenAPI::OptionalParam<QString> &employee_department = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &employee_gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDate> &employee_hire_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &employee_position = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &employee_weekly_hours = ::OpenAPI::OptionalParam<double>());

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void companyTimeOffTypesGet(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  start_date QDate [optional]
    * @param[in]  end_date QDate [optional]
    * @param[in]  updated_from QString [optional]
    * @param[in]  updated_to QString [optional]
    * @param[in]  employees QList<qint32> [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void companyTimeOffsGet(const ::OpenAPI::OptionalParam<QDate> &start_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QDate> &end_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QString> &updated_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &updated_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<qint32>> &employees = ::OpenAPI::OptionalParam<QList<qint32>>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void companyTimeOffsIdDelete(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void companyTimeOffsIdGet(const qint32 &id);

    /**
    * @param[in]  oai_create_time_off_period_request OAICreateTimeOffPeriodRequest [required]
    */
    virtual void companyTimeOffsPost(const OAICreateTimeOffPeriodRequest &oai_create_time_off_period_request);


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

    void companyAttendancesGetCallback(OAIHttpRequestWorker *worker);
    void companyAttendancesIdDeleteCallback(OAIHttpRequestWorker *worker);
    void companyAttendancesIdPatchCallback(OAIHttpRequestWorker *worker);
    void companyAttendancesPostCallback(OAIHttpRequestWorker *worker);
    void companyEmployeesEmployeeIdGetCallback(OAIHttpRequestWorker *worker);
    void companyEmployeesEmployeeIdProfilePictureWidthGetCallback(OAIHttpRequestWorker *worker);
    void companyEmployeesGetCallback(OAIHttpRequestWorker *worker);
    void companyEmployeesPostCallback(OAIHttpRequestWorker *worker);
    void companyTimeOffTypesGetCallback(OAIHttpRequestWorker *worker);
    void companyTimeOffsGetCallback(OAIHttpRequestWorker *worker);
    void companyTimeOffsIdDeleteCallback(OAIHttpRequestWorker *worker);
    void companyTimeOffsIdGetCallback(OAIHttpRequestWorker *worker);
    void companyTimeOffsPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void companyAttendancesGetSignal(OAIAttendancePeriodsResponse summary);
    void companyAttendancesIdDeleteSignal(OAIResponse summary);
    void companyAttendancesIdPatchSignal(OAIResponse summary);
    void companyAttendancesPostSignal(OAINewAttendancePeriodResponse summary);
    void companyEmployeesEmployeeIdGetSignal(OAIEmployeeResponse summary);
    void companyEmployeesEmployeeIdProfilePictureWidthGetSignal(OAIHttpFileElement summary);
    void companyEmployeesGetSignal(OAIEmployeesResponse summary);
    void companyEmployeesPostSignal(OAIResponse summary);
    void companyTimeOffTypesGetSignal(OAI_company_time_off_types_get_200_response summary);
    void companyTimeOffsGetSignal(OAIAbsencePeriodsResponse summary);
    void companyTimeOffsIdDeleteSignal(OAIResponse summary);
    void companyTimeOffsIdGetSignal(OAIObject summary);
    void companyTimeOffsPostSignal(OAI_company_time_offs_post_201_response summary);


    void companyAttendancesGetSignalFull(OAIHttpRequestWorker *worker, OAIAttendancePeriodsResponse summary);
    void companyAttendancesIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIResponse summary);
    void companyAttendancesIdPatchSignalFull(OAIHttpRequestWorker *worker, OAIResponse summary);
    void companyAttendancesPostSignalFull(OAIHttpRequestWorker *worker, OAINewAttendancePeriodResponse summary);
    void companyEmployeesEmployeeIdGetSignalFull(OAIHttpRequestWorker *worker, OAIEmployeeResponse summary);
    void companyEmployeesEmployeeIdProfilePictureWidthGetSignalFull(OAIHttpRequestWorker *worker, OAIHttpFileElement summary);
    void companyEmployeesGetSignalFull(OAIHttpRequestWorker *worker, OAIEmployeesResponse summary);
    void companyEmployeesPostSignalFull(OAIHttpRequestWorker *worker, OAIResponse summary);
    void companyTimeOffTypesGetSignalFull(OAIHttpRequestWorker *worker, OAI_company_time_off_types_get_200_response summary);
    void companyTimeOffsGetSignalFull(OAIHttpRequestWorker *worker, OAIAbsencePeriodsResponse summary);
    void companyTimeOffsIdDeleteSignalFull(OAIHttpRequestWorker *worker, OAIResponse summary);
    void companyTimeOffsIdGetSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void companyTimeOffsPostSignalFull(OAIHttpRequestWorker *worker, OAI_company_time_offs_post_201_response summary);

    Q_DECL_DEPRECATED_X("Use companyAttendancesGetSignalError() instead")
    void companyAttendancesGetSignalE(OAIAttendancePeriodsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesGetSignalError(OAIAttendancePeriodsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyAttendancesIdDeleteSignalError() instead")
    void companyAttendancesIdDeleteSignalE(OAIResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesIdDeleteSignalError(OAIResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyAttendancesIdPatchSignalError() instead")
    void companyAttendancesIdPatchSignalE(OAIResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesIdPatchSignalError(OAIResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyAttendancesPostSignalError() instead")
    void companyAttendancesPostSignalE(OAINewAttendancePeriodResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesPostSignalError(OAINewAttendancePeriodResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesEmployeeIdGetSignalError() instead")
    void companyEmployeesEmployeeIdGetSignalE(OAIEmployeeResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesEmployeeIdGetSignalError(OAIEmployeeResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesEmployeeIdProfilePictureWidthGetSignalError() instead")
    void companyEmployeesEmployeeIdProfilePictureWidthGetSignalE(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesEmployeeIdProfilePictureWidthGetSignalError(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesGetSignalError() instead")
    void companyEmployeesGetSignalE(OAIEmployeesResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesGetSignalError(OAIEmployeesResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesPostSignalError() instead")
    void companyEmployeesPostSignalE(OAIResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesPostSignalError(OAIResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffTypesGetSignalError() instead")
    void companyTimeOffTypesGetSignalE(OAI_company_time_off_types_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffTypesGetSignalError(OAI_company_time_off_types_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsGetSignalError() instead")
    void companyTimeOffsGetSignalE(OAIAbsencePeriodsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsGetSignalError(OAIAbsencePeriodsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsIdDeleteSignalError() instead")
    void companyTimeOffsIdDeleteSignalE(OAIResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsIdDeleteSignalError(OAIResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsIdGetSignalError() instead")
    void companyTimeOffsIdGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsIdGetSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsPostSignalError() instead")
    void companyTimeOffsPostSignalE(OAI_company_time_offs_post_201_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsPostSignalError(OAI_company_time_offs_post_201_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use companyAttendancesGetSignalErrorFull() instead")
    void companyAttendancesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyAttendancesIdDeleteSignalErrorFull() instead")
    void companyAttendancesIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyAttendancesIdPatchSignalErrorFull() instead")
    void companyAttendancesIdPatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesIdPatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyAttendancesPostSignalErrorFull() instead")
    void companyAttendancesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyAttendancesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesEmployeeIdGetSignalErrorFull() instead")
    void companyEmployeesEmployeeIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesEmployeeIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesEmployeeIdProfilePictureWidthGetSignalErrorFull() instead")
    void companyEmployeesEmployeeIdProfilePictureWidthGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesEmployeeIdProfilePictureWidthGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesGetSignalErrorFull() instead")
    void companyEmployeesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyEmployeesPostSignalErrorFull() instead")
    void companyEmployeesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyEmployeesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffTypesGetSignalErrorFull() instead")
    void companyTimeOffTypesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffTypesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsGetSignalErrorFull() instead")
    void companyTimeOffsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsIdDeleteSignalErrorFull() instead")
    void companyTimeOffsIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsIdGetSignalErrorFull() instead")
    void companyTimeOffsIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use companyTimeOffsPostSignalErrorFull() instead")
    void companyTimeOffsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void companyTimeOffsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
