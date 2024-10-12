/**
 * StorageManagementClient
 * The Admin Storage Management Client.
 *
 * The version of the OpenAPI document: 2015-12-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITableServices_ListMetricDefinitions_200_response_value_inner_name.h
 *
 * Localizable string.
 */

#ifndef OAITableServices_ListMetricDefinitions_200_response_value_inner_name_H
#define OAITableServices_ListMetricDefinitions_200_response_value_inner_name_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITableServices_ListMetricDefinitions_200_response_value_inner_name : public OAIObject {
public:
    OAITableServices_ListMetricDefinitions_200_response_value_inner_name();
    OAITableServices_ListMetricDefinitions_200_response_value_inner_name(QString json);
    ~OAITableServices_ListMetricDefinitions_200_response_value_inner_name() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLocalizedValue() const;
    void setLocalizedValue(const QString &localized_value);
    bool is_localized_value_Set() const;
    bool is_localized_value_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_localized_value;
    bool m_localized_value_isSet;
    bool m_localized_value_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITableServices_ListMetricDefinitions_200_response_value_inner_name)

#endif // OAITableServices_ListMetricDefinitions_200_response_value_inner_name_H
