/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAINamesResponse.h
 *
 * 
 */

#ifndef OAINamesResponse_H
#define OAINamesResponse_H

#include <QJsonObject>

#include "OAIEntityName.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEntityName;

class OAINamesResponse : public OAIObject {
public:
    OAINamesResponse();
    OAINamesResponse(QString json);
    ~OAINamesResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIEntityName> getEntities() const;
    void setEntities(const QList<OAIEntityName> &entities);
    bool is_entities_Set() const;
    bool is_entities_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIEntityName> m_entities;
    bool m_entities_isSet;
    bool m_entities_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINamesResponse)

#endif // OAINamesResponse_H
