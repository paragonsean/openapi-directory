/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner.h
 *
 * 
 */

#ifndef OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_H
#define OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_H

#include <QJsonObject>

#include "OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_version_types.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_version_types;

class OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner : public OAIObject {
public:
    OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner();
    OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner(QString json);
    ~OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_version_types getVersionTypes() const;
    void setVersionTypes(const OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_version_types &version_types);
    bool is_version_types_Set() const;
    bool is_version_types_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_version_types m_version_types;
    bool m_version_types_isSet;
    bool m_version_types_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner)

#endif // OAIAvailability_mixin_availability_inner_version_types_version_type_inner_version_type_inner_availability_inner_H
