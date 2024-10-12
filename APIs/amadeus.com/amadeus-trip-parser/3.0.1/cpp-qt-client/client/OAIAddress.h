/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAddress.h
 *
 * Address information
 */

#ifndef OAIAddress_H
#define OAIAddress_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddress : public OAIObject {
public:
    OAIAddress();
    OAIAddress(QString json);
    ~OAIAddress() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCategory() const;
    void setCategory(const QString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QString getCityName() const;
    void setCityName(const QString &city_name);
    bool is_city_name_Set() const;
    bool is_city_name_Valid() const;

    QString getCountryCode() const;
    void setCountryCode(const QString &country_code);
    bool is_country_code_Set() const;
    bool is_country_code_Valid() const;

    QList<QString> getLines() const;
    void setLines(const QList<QString> &lines);
    bool is_lines_Set() const;
    bool is_lines_Valid() const;

    QString getPostalBox() const;
    void setPostalBox(const QString &postal_box);
    bool is_postal_box_Set() const;
    bool is_postal_box_Valid() const;

    QString getPostalCode() const;
    void setPostalCode(const QString &postal_code);
    bool is_postal_code_Set() const;
    bool is_postal_code_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStateCode() const;
    void setStateCode(const QString &state_code);
    bool is_state_code_Set() const;
    bool is_state_code_Valid() const;

    QString getText() const;
    void setText(const QString &text);
    bool is_text_Set() const;
    bool is_text_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QString m_city_name;
    bool m_city_name_isSet;
    bool m_city_name_isValid;

    QString m_country_code;
    bool m_country_code_isSet;
    bool m_country_code_isValid;

    QList<QString> m_lines;
    bool m_lines_isSet;
    bool m_lines_isValid;

    QString m_postal_box;
    bool m_postal_box_isSet;
    bool m_postal_box_isValid;

    QString m_postal_code;
    bool m_postal_code_isSet;
    bool m_postal_code_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_state_code;
    bool m_state_code_isSet;
    bool m_state_code_isValid;

    QString m_text;
    bool m_text_isSet;
    bool m_text_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddress)

#endif // OAIAddress_H
