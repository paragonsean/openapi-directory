/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEventVenue.h
 *
 * 
 */

#ifndef OAIEventVenue_H
#define OAIEventVenue_H

#include <QJsonObject>

#include "OAILocalizedString.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILocalizedString;

class OAIEventVenue : public OAIObject {
public:
    OAIEventVenue();
    OAIEventVenue(QString json);
    ~OAIEventVenue() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAILocalizedString getAddress() const;
    void setAddress(const OAILocalizedString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QString getKind() const;
    void setKind(const QString &kind);
    bool is_kind_Set() const;
    bool is_kind_Valid() const;

    OAILocalizedString getName() const;
    void setName(const OAILocalizedString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAILocalizedString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QString m_kind;
    bool m_kind_isSet;
    bool m_kind_isValid;

    OAILocalizedString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEventVenue)

#endif // OAIEventVenue_H
