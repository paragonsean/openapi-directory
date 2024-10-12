/**
 * Open States API v3
 *  * [More documentation](https://docs.openstates.org/en/latest/api/v3/index.html) * [Register for an account](https://openstates.org/accounts/signup/)   **We are currently working to restore experimental support for committees & events.**  During this period please note that data is not yet available for all states and the exact format of the new endpoints may change slightly depending on user feedback.  If you have any issues or questions use our [GitHub Issues](https://github.com/openstates/issues/issues) to give feedback. 
 *
 * The version of the OpenAPI document: 2021.11.12
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICommitteeMembership.h
 *
 * 
 */

#ifndef OAICommitteeMembership_H
#define OAICommitteeMembership_H

#include <QJsonObject>

#include "OAICompactPerson.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICompactPerson;

class OAICommitteeMembership : public OAIObject {
public:
    OAICommitteeMembership();
    OAICommitteeMembership(QString json);
    ~OAICommitteeMembership() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICompactPerson getPerson() const;
    void setPerson(const OAICompactPerson &person);
    bool is_person_Set() const;
    bool is_person_Valid() const;

    QString getPersonName() const;
    void setPersonName(const QString &person_name);
    bool is_person_name_Set() const;
    bool is_person_name_Valid() const;

    QString getRole() const;
    void setRole(const QString &role);
    bool is_role_Set() const;
    bool is_role_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICompactPerson m_person;
    bool m_person_isSet;
    bool m_person_isValid;

    QString m_person_name;
    bool m_person_name_isSet;
    bool m_person_name_isValid;

    QString m_role;
    bool m_role_isSet;
    bool m_role_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICommitteeMembership)

#endif // OAICommitteeMembership_H
