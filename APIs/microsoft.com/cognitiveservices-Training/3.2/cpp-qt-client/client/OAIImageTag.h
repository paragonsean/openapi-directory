/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageTag.h
 *
 * 
 */

#ifndef OAIImageTag_H
#define OAIImageTag_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImageTag : public OAIObject {
public:
    OAIImageTag();
    OAIImageTag(QString json);
    ~OAIImageTag() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreated() const;
    void setCreated(const QDateTime &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QString getTagId() const;
    void setTagId(const QString &tag_id);
    bool is_tag_id_Set() const;
    bool is_tag_id_Valid() const;

    QString getTagName() const;
    void setTagName(const QString &tag_name);
    bool is_tag_name_Set() const;
    bool is_tag_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_tag_id;
    bool m_tag_id_isSet;
    bool m_tag_id_isValid;

    QString m_tag_name;
    bool m_tag_name_isSet;
    bool m_tag_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageTag)

#endif // OAIImageTag_H
