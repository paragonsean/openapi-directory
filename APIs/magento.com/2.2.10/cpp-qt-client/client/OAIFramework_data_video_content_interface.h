/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFramework_data_video_content_interface.h
 *
 * Video Content data interface
 */

#ifndef OAIFramework_data_video_content_interface_H
#define OAIFramework_data_video_content_interface_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFramework_data_video_content_interface : public OAIObject {
public:
    OAIFramework_data_video_content_interface();
    OAIFramework_data_video_content_interface(QString json);
    ~OAIFramework_data_video_content_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getMediaType() const;
    void setMediaType(const QString &media_type);
    bool is_media_type_Set() const;
    bool is_media_type_Valid() const;

    QString getVideoDescription() const;
    void setVideoDescription(const QString &video_description);
    bool is_video_description_Set() const;
    bool is_video_description_Valid() const;

    QString getVideoMetadata() const;
    void setVideoMetadata(const QString &video_metadata);
    bool is_video_metadata_Set() const;
    bool is_video_metadata_Valid() const;

    QString getVideoProvider() const;
    void setVideoProvider(const QString &video_provider);
    bool is_video_provider_Set() const;
    bool is_video_provider_Valid() const;

    QString getVideoTitle() const;
    void setVideoTitle(const QString &video_title);
    bool is_video_title_Set() const;
    bool is_video_title_Valid() const;

    QString getVideoUrl() const;
    void setVideoUrl(const QString &video_url);
    bool is_video_url_Set() const;
    bool is_video_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_media_type;
    bool m_media_type_isSet;
    bool m_media_type_isValid;

    QString m_video_description;
    bool m_video_description_isSet;
    bool m_video_description_isValid;

    QString m_video_metadata;
    bool m_video_metadata_isSet;
    bool m_video_metadata_isValid;

    QString m_video_provider;
    bool m_video_provider_isSet;
    bool m_video_provider_isValid;

    QString m_video_title;
    bool m_video_title_isSet;
    bool m_video_title_isValid;

    QString m_video_url;
    bool m_video_url_isSet;
    bool m_video_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFramework_data_video_content_interface)

#endif // OAIFramework_data_video_content_interface_H
