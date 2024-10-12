/**
 * Azure Data Migration Service Resource Provider
 * The Data Migration Service helps people migrate their data from on-premise database servers to Azure, or from older database software to newer software. The service manages one or more workers that are joined to a customer's virtual network, which is assumed to provide connectivity to their databases. To avoid frequent updates to the resource provider, data migration tasks are implemented by the resource provider in a generic way as task resources, each of which has a task type (which identifies the type of work to run), input, and output. The client is responsible for providing appropriate task type and inputs, which will be passed through unexamined to the machines that implement the functionality, and for understanding the output, which is passed back unexamined to the client.
 *
 * The version of the OpenAPI document: 2018-03-15-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITasks_Get_200_response.h
 *
 * A task resource
 */

#ifndef OAITasks_Get_200_response_H
#define OAITasks_Get_200_response_H

#include <QJsonObject>

#include "OAITasks_List_200_response_value_inner_properties.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITasks_List_200_response_value_inner_properties;

class OAITasks_Get_200_response : public OAIObject {
public:
    OAITasks_Get_200_response();
    OAITasks_Get_200_response(QString json);
    ~OAITasks_Get_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEtag() const;
    void setEtag(const QString &etag);
    bool is_etag_Set() const;
    bool is_etag_Valid() const;

    OAITasks_List_200_response_value_inner_properties getProperties() const;
    void setProperties(const OAITasks_List_200_response_value_inner_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_etag;
    bool m_etag_isSet;
    bool m_etag_isValid;

    OAITasks_List_200_response_value_inner_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITasks_Get_200_response)

#endif // OAITasks_Get_200_response_H
