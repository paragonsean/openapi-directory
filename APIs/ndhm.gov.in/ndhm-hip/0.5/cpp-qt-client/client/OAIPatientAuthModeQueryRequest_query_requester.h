/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPatientAuthModeQueryRequest_query_requester.h
 *
 * 
 */

#ifndef OAIPatientAuthModeQueryRequest_query_requester_H
#define OAIPatientAuthModeQueryRequest_query_requester_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPatientAuthModeQueryRequest_query_requester : public OAIObject {
public:
    OAIPatientAuthModeQueryRequest_query_requester();
    OAIPatientAuthModeQueryRequest_query_requester(QString json);
    ~OAIPatientAuthModeQueryRequest_query_requester() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientAuthModeQueryRequest_query_requester)

#endif // OAIPatientAuthModeQueryRequest_query_requester_H
