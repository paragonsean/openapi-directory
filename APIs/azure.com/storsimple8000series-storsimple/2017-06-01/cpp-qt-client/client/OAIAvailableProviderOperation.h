/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAvailableProviderOperation.h
 *
 * Represents available provider operation.
 */

#ifndef OAIAvailableProviderOperation_H
#define OAIAvailableProviderOperation_H

#include <QJsonObject>

#include "OAIAvailableProviderOperationDisplay.h"
#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAvailableProviderOperationDisplay;

class OAIAvailableProviderOperation : public OAIObject {
public:
    OAIAvailableProviderOperation();
    OAIAvailableProviderOperation(QString json);
    ~OAIAvailableProviderOperation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAvailableProviderOperationDisplay getDisplay() const;
    void setDisplay(const OAIAvailableProviderOperationDisplay &display);
    bool is_display_Set() const;
    bool is_display_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOrigin() const;
    void setOrigin(const QString &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    OAIObject getProperties() const;
    void setProperties(const OAIObject &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAvailableProviderOperationDisplay m_display;
    bool m_display_isSet;
    bool m_display_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;

    OAIObject m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAvailableProviderOperation)

#endif // OAIAvailableProviderOperation_H
