/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEncryptionPasswordPolicies.h
 *
 * Encryption password policies
 */

#ifndef OAIEncryptionPasswordPolicies_H
#define OAIEncryptionPasswordPolicies_H

#include <QJsonObject>

#include "OAICharacterRules.h"
#include "OAIUserInfo.h"
#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICharacterRules;
class OAIUserInfo;

class OAIEncryptionPasswordPolicies : public OAIObject {
public:
    OAIEncryptionPasswordPolicies();
    OAIEncryptionPasswordPolicies(QString json);
    ~OAIEncryptionPasswordPolicies() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICharacterRules getCharacterRules() const;
    void setCharacterRules(const OAICharacterRules &character_rules);
    bool is_character_rules_Set() const;
    bool is_character_rules_Valid() const;

    qint32 getMinLength() const;
    void setMinLength(const qint32 &min_length);
    bool is_min_length_Set() const;
    bool is_min_length_Valid() const;

    bool isRejectKeyboardPatterns() const;
    void setRejectKeyboardPatterns(const bool &reject_keyboard_patterns);
    bool is_reject_keyboard_patterns_Set() const;
    bool is_reject_keyboard_patterns_Valid() const;

    bool isRejectUserInfo() const;
    void setRejectUserInfo(const bool &reject_user_info);
    bool is_reject_user_info_Set() const;
    bool is_reject_user_info_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    OAIUserInfo getUpdatedBy() const;
    void setUpdatedBy(const OAIUserInfo &updated_by);
    bool is_updated_by_Set() const;
    bool is_updated_by_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICharacterRules m_character_rules;
    bool m_character_rules_isSet;
    bool m_character_rules_isValid;

    qint32 m_min_length;
    bool m_min_length_isSet;
    bool m_min_length_isValid;

    bool m_reject_keyboard_patterns;
    bool m_reject_keyboard_patterns_isSet;
    bool m_reject_keyboard_patterns_isValid;

    bool m_reject_user_info;
    bool m_reject_user_info_isSet;
    bool m_reject_user_info_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    OAIUserInfo m_updated_by;
    bool m_updated_by_isSet;
    bool m_updated_by_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEncryptionPasswordPolicies)

#endif // OAIEncryptionPasswordPolicies_H
