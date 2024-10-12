/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomerUpdate.h
 *
 * 
 */

#ifndef OAICustomerUpdate_H
#define OAICustomerUpdate_H

#include <QJsonObject>

#include "OAICustomerUpdate_address_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICustomerUpdate_address_inner;

class OAICustomerUpdate : public OAIObject {
public:
    OAICustomerUpdate();
    OAICustomerUpdate(QString json);
    ~OAICustomerUpdate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAICustomerUpdate_address_inner> getAddress() const;
    void setAddress(const QList<OAICustomerUpdate_address_inner> &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getGroupId() const;
    void setGroupId(const QString &group_id);
    bool is_group_id_Set() const;
    bool is_group_id_Valid() const;

    QString getGroupIds() const;
    void setGroupIds(const QString &group_ids);
    bool is_group_ids_Set() const;
    bool is_group_ids_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    bool isNewsLetterSubscription() const;
    void setNewsLetterSubscription(const bool &news_letter_subscription);
    bool is_news_letter_subscription_Set() const;
    bool is_news_letter_subscription_Valid() const;

    QString getPhone() const;
    void setPhone(const QString &phone);
    bool is_phone_Set() const;
    bool is_phone_Valid() const;

    QString getTags() const;
    void setTags(const QString &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAICustomerUpdate_address_inner> m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_group_id;
    bool m_group_id_isSet;
    bool m_group_id_isValid;

    QString m_group_ids;
    bool m_group_ids_isSet;
    bool m_group_ids_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    bool m_news_letter_subscription;
    bool m_news_letter_subscription_isSet;
    bool m_news_letter_subscription_isValid;

    QString m_phone;
    bool m_phone_isSet;
    bool m_phone_isValid;

    QString m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomerUpdate)

#endif // OAICustomerUpdate_H
