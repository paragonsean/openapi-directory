/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIName.h
 *
 * name
 */

#ifndef OAIName_H
#define OAIName_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIName : public OAIObject {
public:
    OAIName();
    OAIName(QString json);
    ~OAIName() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getMiddleName() const;
    void setMiddleName(const QString &middle_name);
    bool is_middle_name_Set() const;
    bool is_middle_name_Valid() const;

    QString getSecondLastName() const;
    void setSecondLastName(const QString &second_last_name);
    bool is_second_last_name_Set() const;
    bool is_second_last_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_middle_name;
    bool m_middle_name_isSet;
    bool m_middle_name_isValid;

    QString m_second_last_name;
    bool m_second_last_name_isSet;
    bool m_second_last_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIName)

#endif // OAIName_H
