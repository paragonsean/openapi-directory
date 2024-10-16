/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIManagedFieldsEntry.h
 *
 * ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to.
 */

#ifndef OAIManagedFieldsEntry_H
#define OAIManagedFieldsEntry_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIManagedFieldsEntry : public OAIObject {
public:
    OAIManagedFieldsEntry();
    OAIManagedFieldsEntry(QString json);
    ~OAIManagedFieldsEntry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getApiVersion() const;
    void setApiVersion(const QString &api_version);
    bool is_api_version_Set() const;
    bool is_api_version_Valid() const;

    QString getFieldsType() const;
    void setFieldsType(const QString &fields_type);
    bool is_fields_type_Set() const;
    bool is_fields_type_Valid() const;

    OAIObject getFieldsV1() const;
    void setFieldsV1(const OAIObject &fields_v1);
    bool is_fields_v1_Set() const;
    bool is_fields_v1_Valid() const;

    QString getManager() const;
    void setManager(const QString &manager);
    bool is_manager_Set() const;
    bool is_manager_Valid() const;

    QString getOperation() const;
    void setOperation(const QString &operation);
    bool is_operation_Set() const;
    bool is_operation_Valid() const;

    OAIObject getTime() const;
    void setTime(const OAIObject &time);
    bool is_time_Set() const;
    bool is_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_api_version;
    bool m_api_version_isSet;
    bool m_api_version_isValid;

    QString m_fields_type;
    bool m_fields_type_isSet;
    bool m_fields_type_isValid;

    OAIObject m_fields_v1;
    bool m_fields_v1_isSet;
    bool m_fields_v1_isValid;

    QString m_manager;
    bool m_manager_isSet;
    bool m_manager_isValid;

    QString m_operation;
    bool m_operation_isSet;
    bool m_operation_isValid;

    OAIObject m_time;
    bool m_time_isSet;
    bool m_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIManagedFieldsEntry)

#endif // OAIManagedFieldsEntry_H
