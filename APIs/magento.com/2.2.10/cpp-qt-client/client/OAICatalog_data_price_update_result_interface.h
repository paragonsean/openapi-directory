/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICatalog_data_price_update_result_interface.h
 *
 * Interface returned in case of incorrect price passed to efficient price API.
 */

#ifndef OAICatalog_data_price_update_result_interface_H
#define OAICatalog_data_price_update_result_interface_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICatalog_data_price_update_result_interface : public OAIObject {
public:
    OAICatalog_data_price_update_result_interface();
    OAICatalog_data_price_update_result_interface(QString json);
    ~OAICatalog_data_price_update_result_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QList<QString> getParameters() const;
    void setParameters(const QList<QString> &parameters);
    bool is_parameters_Set() const;
    bool is_parameters_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QList<QString> m_parameters;
    bool m_parameters_isSet;
    bool m_parameters_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_price_update_result_interface)

#endif // OAICatalog_data_price_update_result_interface_H
