/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAuthAccountAadhaarBioRequest.h
 *
 * 
 */

#ifndef OAIAuthAccountAadhaarBioRequest_H
#define OAIAuthAccountAadhaarBioRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAuthAccountAadhaarBioRequest : public OAIObject {
public:
    OAIAuthAccountAadhaarBioRequest();
    OAIAuthAccountAadhaarBioRequest(QString json);
    ~OAIAuthAccountAadhaarBioRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAuthType() const;
    void setAuthType(const QString &auth_type);
    bool is_auth_type_Set() const;
    bool is_auth_type_Valid() const;

    QString getBioType() const;
    void setBioType(const QString &bio_type);
    bool is_bio_type_Set() const;
    bool is_bio_type_Valid() const;

    QString getPid() const;
    void setPid(const QString &pid);
    bool is_pid_Set() const;
    bool is_pid_Valid() const;

    QString getTxnId() const;
    void setTxnId(const QString &txn_id);
    bool is_txn_id_Set() const;
    bool is_txn_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_auth_type;
    bool m_auth_type_isSet;
    bool m_auth_type_isValid;

    QString m_bio_type;
    bool m_bio_type_isSet;
    bool m_bio_type_isValid;

    QString m_pid;
    bool m_pid_isSet;
    bool m_pid_isValid;

    QString m_txn_id;
    bool m_txn_id_isSet;
    bool m_txn_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAuthAccountAadhaarBioRequest)

#endif // OAIAuthAccountAadhaarBioRequest_H
