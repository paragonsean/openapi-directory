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
 * OAIQuote_data_total_segment_interface.h
 *
 * Interface TotalsInterface
 */

#ifndef OAIQuote_data_total_segment_interface_H
#define OAIQuote_data_total_segment_interface_H

#include <QJsonObject>

#include "OAIQuote_data_total_segment_extension_interface.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQuote_data_total_segment_extension_interface;

class OAIQuote_data_total_segment_interface : public OAIObject {
public:
    OAIQuote_data_total_segment_interface();
    OAIQuote_data_total_segment_interface(QString json);
    ~OAIQuote_data_total_segment_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArea() const;
    void setArea(const QString &area);
    bool is_area_Set() const;
    bool is_area_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    OAIQuote_data_total_segment_extension_interface getExtensionAttributes() const;
    void setExtensionAttributes(const OAIQuote_data_total_segment_extension_interface &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    double getValue() const;
    void setValue(const double &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_area;
    bool m_area_isSet;
    bool m_area_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    OAIQuote_data_total_segment_extension_interface m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    double m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuote_data_total_segment_interface)

#endif // OAIQuote_data_total_segment_interface_H
