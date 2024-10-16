/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProfiles_inner_statistics.h
 *
 * 
 */

#ifndef OAIProfiles_inner_statistics_H
#define OAIProfiles_inner_statistics_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProfiles_inner_statistics : public OAIObject {
public:
    OAIProfiles_inner_statistics();
    OAIProfiles_inner_statistics(QString json);
    ~OAIProfiles_inner_statistics() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getConnections() const;
    void setConnections(const double &connections);
    bool is_connections_Set() const;
    bool is_connections_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_connections;
    bool m_connections_isSet;
    bool m_connections_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProfiles_inner_statistics)

#endif // OAIProfiles_inner_statistics_H
