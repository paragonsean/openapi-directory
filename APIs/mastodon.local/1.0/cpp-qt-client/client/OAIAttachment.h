/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAttachment.h
 *
 * Represents a file or media attachment that can be added to a status.
 */

#ifndef OAIAttachment_H
#define OAIAttachment_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAttachment : public OAIObject {
public:
    OAIAttachment();
    OAIAttachment(QString json);
    ~OAIAttachment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBlurhash() const;
    void setBlurhash(const QString &blurhash);
    bool is_blurhash_Set() const;
    bool is_blurhash_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIObject getMeta() const;
    void setMeta(const OAIObject &meta);
    bool is_meta_Set() const;
    bool is_meta_Valid() const;

    QString getPreviewUrl() const;
    void setPreviewUrl(const QString &preview_url);
    bool is_preview_url_Set() const;
    bool is_preview_url_Valid() const;

    QString getRemoteUrl() const;
    void setRemoteUrl(const QString &remote_url);
    bool is_remote_url_Set() const;
    bool is_remote_url_Valid() const;

    Q_DECL_DEPRECATED QString getTextUrl() const;
    Q_DECL_DEPRECATED void setTextUrl(const QString &text_url);
    Q_DECL_DEPRECATED bool is_text_url_Set() const;
    Q_DECL_DEPRECATED bool is_text_url_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_blurhash;
    bool m_blurhash_isSet;
    bool m_blurhash_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIObject m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;

    QString m_preview_url;
    bool m_preview_url_isSet;
    bool m_preview_url_isValid;

    QString m_remote_url;
    bool m_remote_url_isSet;
    bool m_remote_url_isValid;

    QString m_text_url;
    bool m_text_url_isSet;
    bool m_text_url_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAttachment)

#endif // OAIAttachment_H
