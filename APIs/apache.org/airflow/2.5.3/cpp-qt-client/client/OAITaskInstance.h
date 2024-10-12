/**
 * Airflow API (Stable)
 * # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 
 *
 * The version of the OpenAPI document: 2.5.3
 * Contact: dev@airflow.apache.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITaskInstance.h
 *
 * 
 */

#ifndef OAITaskInstance_H
#define OAITaskInstance_H

#include <QJsonObject>

#include "OAIJob.h"
#include "OAIObject.h"
#include "OAISLAMiss.h"
#include "OAITaskState.h"
#include "OAITrigger.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISLAMiss;
class OAITrigger;
class OAIJob;

class OAITaskInstance : public OAIObject {
public:
    OAITaskInstance();
    OAITaskInstance(QString json);
    ~OAITaskInstance() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDagId() const;
    void setDagId(const QString &dag_id);
    bool is_dag_id_Set() const;
    bool is_dag_id_Valid() const;

    QString getDagRunId() const;
    void setDagRunId(const QString &dag_run_id);
    bool is_dag_run_id_Set() const;
    bool is_dag_run_id_Valid() const;

    double getDuration() const;
    void setDuration(const double &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    QString getEndDate() const;
    void setEndDate(const QString &end_date);
    bool is_end_date_Set() const;
    bool is_end_date_Valid() const;

    QString getExecutionDate() const;
    void setExecutionDate(const QString &execution_date);
    bool is_execution_date_Set() const;
    bool is_execution_date_Valid() const;

    QString getExecutorConfig() const;
    void setExecutorConfig(const QString &executor_config);
    bool is_executor_config_Set() const;
    bool is_executor_config_Valid() const;

    QString getHostname() const;
    void setHostname(const QString &hostname);
    bool is_hostname_Set() const;
    bool is_hostname_Valid() const;

    qint32 getMapIndex() const;
    void setMapIndex(const qint32 &map_index);
    bool is_map_index_Set() const;
    bool is_map_index_Valid() const;

    qint32 getMaxTries() const;
    void setMaxTries(const qint32 &max_tries);
    bool is_max_tries_Set() const;
    bool is_max_tries_Valid() const;

    QString getNote() const;
    void setNote(const QString &note);
    bool is_note_Set() const;
    bool is_note_Valid() const;

    QString getROperator() const;
    void setROperator(const QString &r_operator);
    bool is_r_operator_Set() const;
    bool is_r_operator_Valid() const;

    qint32 getPid() const;
    void setPid(const qint32 &pid);
    bool is_pid_Set() const;
    bool is_pid_Valid() const;

    QString getPool() const;
    void setPool(const QString &pool);
    bool is_pool_Set() const;
    bool is_pool_Valid() const;

    qint32 getPoolSlots() const;
    void setPoolSlots(const qint32 &pool_slots);
    bool is_pool_slots_Set() const;
    bool is_pool_slots_Valid() const;

    qint32 getPriorityWeight() const;
    void setPriorityWeight(const qint32 &priority_weight);
    bool is_priority_weight_Set() const;
    bool is_priority_weight_Valid() const;

    QString getQueue() const;
    void setQueue(const QString &queue);
    bool is_queue_Set() const;
    bool is_queue_Valid() const;

    QString getQueuedWhen() const;
    void setQueuedWhen(const QString &queued_when);
    bool is_queued_when_Set() const;
    bool is_queued_when_Valid() const;

    OAIObject getRenderedFields() const;
    void setRenderedFields(const OAIObject &rendered_fields);
    bool is_rendered_fields_Set() const;
    bool is_rendered_fields_Valid() const;

    OAISLAMiss getSlaMiss() const;
    void setSlaMiss(const OAISLAMiss &sla_miss);
    bool is_sla_miss_Set() const;
    bool is_sla_miss_Valid() const;

    QString getStartDate() const;
    void setStartDate(const QString &start_date);
    bool is_start_date_Set() const;
    bool is_start_date_Valid() const;

    OAITaskState getState() const;
    void setState(const OAITaskState &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getTaskId() const;
    void setTaskId(const QString &task_id);
    bool is_task_id_Set() const;
    bool is_task_id_Valid() const;

    OAITrigger getTrigger() const;
    void setTrigger(const OAITrigger &trigger);
    bool is_trigger_Set() const;
    bool is_trigger_Valid() const;

    OAIJob getTriggererJob() const;
    void setTriggererJob(const OAIJob &triggerer_job);
    bool is_triggerer_job_Set() const;
    bool is_triggerer_job_Valid() const;

    qint32 getTryNumber() const;
    void setTryNumber(const qint32 &try_number);
    bool is_try_number_Set() const;
    bool is_try_number_Valid() const;

    QString getUnixname() const;
    void setUnixname(const QString &unixname);
    bool is_unixname_Set() const;
    bool is_unixname_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_dag_id;
    bool m_dag_id_isSet;
    bool m_dag_id_isValid;

    QString m_dag_run_id;
    bool m_dag_run_id_isSet;
    bool m_dag_run_id_isValid;

    double m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    QString m_end_date;
    bool m_end_date_isSet;
    bool m_end_date_isValid;

    QString m_execution_date;
    bool m_execution_date_isSet;
    bool m_execution_date_isValid;

    QString m_executor_config;
    bool m_executor_config_isSet;
    bool m_executor_config_isValid;

    QString m_hostname;
    bool m_hostname_isSet;
    bool m_hostname_isValid;

    qint32 m_map_index;
    bool m_map_index_isSet;
    bool m_map_index_isValid;

    qint32 m_max_tries;
    bool m_max_tries_isSet;
    bool m_max_tries_isValid;

    QString m_note;
    bool m_note_isSet;
    bool m_note_isValid;

    QString m_r_operator;
    bool m_r_operator_isSet;
    bool m_r_operator_isValid;

    qint32 m_pid;
    bool m_pid_isSet;
    bool m_pid_isValid;

    QString m_pool;
    bool m_pool_isSet;
    bool m_pool_isValid;

    qint32 m_pool_slots;
    bool m_pool_slots_isSet;
    bool m_pool_slots_isValid;

    qint32 m_priority_weight;
    bool m_priority_weight_isSet;
    bool m_priority_weight_isValid;

    QString m_queue;
    bool m_queue_isSet;
    bool m_queue_isValid;

    QString m_queued_when;
    bool m_queued_when_isSet;
    bool m_queued_when_isValid;

    OAIObject m_rendered_fields;
    bool m_rendered_fields_isSet;
    bool m_rendered_fields_isValid;

    OAISLAMiss m_sla_miss;
    bool m_sla_miss_isSet;
    bool m_sla_miss_isValid;

    QString m_start_date;
    bool m_start_date_isSet;
    bool m_start_date_isValid;

    OAITaskState m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_task_id;
    bool m_task_id_isSet;
    bool m_task_id_isValid;

    OAITrigger m_trigger;
    bool m_trigger_isSet;
    bool m_trigger_isValid;

    OAIJob m_triggerer_job;
    bool m_triggerer_job_isSet;
    bool m_triggerer_job_isValid;

    qint32 m_try_number;
    bool m_try_number_isSet;
    bool m_try_number_isValid;

    QString m_unixname;
    bool m_unixname_isSet;
    bool m_unixname_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITaskInstance)

#endif // OAITaskInstance_H
