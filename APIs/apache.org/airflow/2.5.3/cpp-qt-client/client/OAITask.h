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
 * OAITask.h
 *
 * For details see: [airflow.models.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/index.html#airflow.models.BaseOperator) 
 */

#ifndef OAITask_H
#define OAITask_H

#include <QJsonObject>

#include "OAIClassReference.h"
#include "OAIDAG.h"
#include "OAITask_extra_links_inner.h"
#include "OAITimeDelta.h"
#include "OAITriggerRule.h"
#include "OAIWeightRule.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIClassReference;
class OAITimeDelta;
class OAITask_extra_links_inner;
class OAIDAG;

class OAITask : public OAIObject {
public:
    OAITask();
    OAITask(QString json);
    ~OAITask() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIClassReference getClassRef() const;
    void setClassRef(const OAIClassReference &class_ref);
    bool is_class_ref_Set() const;
    bool is_class_ref_Valid() const;

    bool isDependsOnPast() const;
    void setDependsOnPast(const bool &depends_on_past);
    bool is_depends_on_past_Set() const;
    bool is_depends_on_past_Valid() const;

    QList<QString> getDownstreamTaskIds() const;
    void setDownstreamTaskIds(const QList<QString> &downstream_task_ids);
    bool is_downstream_task_ids_Set() const;
    bool is_downstream_task_ids_Valid() const;

    QDateTime getEndDate() const;
    void setEndDate(const QDateTime &end_date);
    bool is_end_date_Set() const;
    bool is_end_date_Valid() const;

    OAITimeDelta getExecutionTimeout() const;
    void setExecutionTimeout(const OAITimeDelta &execution_timeout);
    bool is_execution_timeout_Set() const;
    bool is_execution_timeout_Valid() const;

    QList<OAITask_extra_links_inner> getExtraLinks() const;
    void setExtraLinks(const QList<OAITask_extra_links_inner> &extra_links);
    bool is_extra_links_Set() const;
    bool is_extra_links_Valid() const;

    bool isIsMapped() const;
    void setIsMapped(const bool &is_mapped);
    bool is_is_mapped_Set() const;
    bool is_is_mapped_Valid() const;

    QString getOwner() const;
    void setOwner(const QString &owner);
    bool is_owner_Set() const;
    bool is_owner_Valid() const;

    QString getPool() const;
    void setPool(const QString &pool);
    bool is_pool_Set() const;
    bool is_pool_Valid() const;

    double getPoolSlots() const;
    void setPoolSlots(const double &pool_slots);
    bool is_pool_slots_Set() const;
    bool is_pool_slots_Valid() const;

    double getPriorityWeight() const;
    void setPriorityWeight(const double &priority_weight);
    bool is_priority_weight_Set() const;
    bool is_priority_weight_Valid() const;

    QString getQueue() const;
    void setQueue(const QString &queue);
    bool is_queue_Set() const;
    bool is_queue_Valid() const;

    double getRetries() const;
    void setRetries(const double &retries);
    bool is_retries_Set() const;
    bool is_retries_Valid() const;

    OAITimeDelta getRetryDelay() const;
    void setRetryDelay(const OAITimeDelta &retry_delay);
    bool is_retry_delay_Set() const;
    bool is_retry_delay_Valid() const;

    bool isRetryExponentialBackoff() const;
    void setRetryExponentialBackoff(const bool &retry_exponential_backoff);
    bool is_retry_exponential_backoff_Set() const;
    bool is_retry_exponential_backoff_Valid() const;

    QDateTime getStartDate() const;
    void setStartDate(const QDateTime &start_date);
    bool is_start_date_Set() const;
    bool is_start_date_Valid() const;

    OAIDAG getSubDag() const;
    void setSubDag(const OAIDAG &sub_dag);
    bool is_sub_dag_Set() const;
    bool is_sub_dag_Valid() const;

    QString getTaskId() const;
    void setTaskId(const QString &task_id);
    bool is_task_id_Set() const;
    bool is_task_id_Valid() const;

    QList<QString> getTemplateFields() const;
    void setTemplateFields(const QList<QString> &template_fields);
    bool is_template_fields_Set() const;
    bool is_template_fields_Valid() const;

    OAITriggerRule getTriggerRule() const;
    void setTriggerRule(const OAITriggerRule &trigger_rule);
    bool is_trigger_rule_Set() const;
    bool is_trigger_rule_Valid() const;

    QString getUiColor() const;
    void setUiColor(const QString &ui_color);
    bool is_ui_color_Set() const;
    bool is_ui_color_Valid() const;

    QString getUiFgcolor() const;
    void setUiFgcolor(const QString &ui_fgcolor);
    bool is_ui_fgcolor_Set() const;
    bool is_ui_fgcolor_Valid() const;

    bool isWaitForDownstream() const;
    void setWaitForDownstream(const bool &wait_for_downstream);
    bool is_wait_for_downstream_Set() const;
    bool is_wait_for_downstream_Valid() const;

    OAIWeightRule getWeightRule() const;
    void setWeightRule(const OAIWeightRule &weight_rule);
    bool is_weight_rule_Set() const;
    bool is_weight_rule_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIClassReference m_class_ref;
    bool m_class_ref_isSet;
    bool m_class_ref_isValid;

    bool m_depends_on_past;
    bool m_depends_on_past_isSet;
    bool m_depends_on_past_isValid;

    QList<QString> m_downstream_task_ids;
    bool m_downstream_task_ids_isSet;
    bool m_downstream_task_ids_isValid;

    QDateTime m_end_date;
    bool m_end_date_isSet;
    bool m_end_date_isValid;

    OAITimeDelta m_execution_timeout;
    bool m_execution_timeout_isSet;
    bool m_execution_timeout_isValid;

    QList<OAITask_extra_links_inner> m_extra_links;
    bool m_extra_links_isSet;
    bool m_extra_links_isValid;

    bool m_is_mapped;
    bool m_is_mapped_isSet;
    bool m_is_mapped_isValid;

    QString m_owner;
    bool m_owner_isSet;
    bool m_owner_isValid;

    QString m_pool;
    bool m_pool_isSet;
    bool m_pool_isValid;

    double m_pool_slots;
    bool m_pool_slots_isSet;
    bool m_pool_slots_isValid;

    double m_priority_weight;
    bool m_priority_weight_isSet;
    bool m_priority_weight_isValid;

    QString m_queue;
    bool m_queue_isSet;
    bool m_queue_isValid;

    double m_retries;
    bool m_retries_isSet;
    bool m_retries_isValid;

    OAITimeDelta m_retry_delay;
    bool m_retry_delay_isSet;
    bool m_retry_delay_isValid;

    bool m_retry_exponential_backoff;
    bool m_retry_exponential_backoff_isSet;
    bool m_retry_exponential_backoff_isValid;

    QDateTime m_start_date;
    bool m_start_date_isSet;
    bool m_start_date_isValid;

    OAIDAG m_sub_dag;
    bool m_sub_dag_isSet;
    bool m_sub_dag_isValid;

    QString m_task_id;
    bool m_task_id_isSet;
    bool m_task_id_isValid;

    QList<QString> m_template_fields;
    bool m_template_fields_isSet;
    bool m_template_fields_isValid;

    OAITriggerRule m_trigger_rule;
    bool m_trigger_rule_isSet;
    bool m_trigger_rule_isValid;

    QString m_ui_color;
    bool m_ui_color_isSet;
    bool m_ui_color_isValid;

    QString m_ui_fgcolor;
    bool m_ui_fgcolor_isSet;
    bool m_ui_fgcolor_isValid;

    bool m_wait_for_downstream;
    bool m_wait_for_downstream_isSet;
    bool m_wait_for_downstream_isValid;

    OAIWeightRule m_weight_rule;
    bool m_weight_rule_isSet;
    bool m_weight_rule_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITask)

#endif // OAITask_H
