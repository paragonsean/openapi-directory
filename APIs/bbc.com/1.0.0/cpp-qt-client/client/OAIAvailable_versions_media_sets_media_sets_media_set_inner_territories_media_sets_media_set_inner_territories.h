/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories.h
 *
 * 
 */

#ifndef OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories_H
#define OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories : public OAIObject {
public:
    OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories();
    OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories(QString json);
    ~OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getTerritory() const;
    void setTerritory(const QList<QString> &territory);
    bool is_territory_Set() const;
    bool is_territory_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_territory;
    bool m_territory_isSet;
    bool m_territory_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories)

#endif // OAIAvailable_versions_media_sets_media_sets_media_set_inner_territories_media_sets_media_set_inner_territories_H
