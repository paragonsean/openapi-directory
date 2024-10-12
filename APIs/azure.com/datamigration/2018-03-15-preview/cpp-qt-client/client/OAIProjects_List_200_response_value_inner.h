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
 * OAIProjects_List_200_response_value_inner.h
 *
 * A project resource
 */

#ifndef OAIProjects_List_200_response_value_inner_H
#define OAIProjects_List_200_response_value_inner_H

#include <QJsonObject>

#include "OAIProjects_List_200_response_value_inner_properties.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIProjects_List_200_response_value_inner_properties;

class OAIProjects_List_200_response_value_inner : public OAIObject {
public:
    OAIProjects_List_200_response_value_inner();
    OAIProjects_List_200_response_value_inner(QString json);
    ~OAIProjects_List_200_response_value_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIProjects_List_200_response_value_inner_properties getProperties() const;
    void setProperties(const OAIProjects_List_200_response_value_inner_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIProjects_List_200_response_value_inner_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjects_List_200_response_value_inner)

#endif // OAIProjects_List_200_response_value_inner_H
