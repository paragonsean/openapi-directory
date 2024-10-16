/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPersonalisedMusicMetaData.h
 *
 * 
 */

#ifndef OAIPersonalisedMusicMetaData_H
#define OAIPersonalisedMusicMetaData_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPersonalisedMusicMetaData : public OAIObject {
public:
    OAIPersonalisedMusicMetaData();
    OAIPersonalisedMusicMetaData(QString json);
    ~OAIPersonalisedMusicMetaData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getKey() const;
    void setKey(const QString &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_key;
    bool m_key_isSet;
    bool m_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPersonalisedMusicMetaData)

#endif // OAIPersonalisedMusicMetaData_H
