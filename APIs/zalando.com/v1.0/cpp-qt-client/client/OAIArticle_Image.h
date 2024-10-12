/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArticle_Image.h
 *
 * Zalando API Article Image Schema
 */

#ifndef OAIArticle_Image_H
#define OAIArticle_Image_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIArticle_Image : public OAIObject {
public:
    OAIArticle_Image();
    OAIArticle_Image(QString json);
    ~OAIArticle_Image() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLargeHdUrl() const;
    void setLargeHdUrl(const QString &large_hd_url);
    bool is_large_hd_url_Set() const;
    bool is_large_hd_url_Valid() const;

    QString getLargeUrl() const;
    void setLargeUrl(const QString &large_url);
    bool is_large_url_Set() const;
    bool is_large_url_Valid() const;

    QString getMediumHdUrl() const;
    void setMediumHdUrl(const QString &medium_hd_url);
    bool is_medium_hd_url_Set() const;
    bool is_medium_hd_url_Valid() const;

    QString getMediumUrl() const;
    void setMediumUrl(const QString &medium_url);
    bool is_medium_url_Set() const;
    bool is_medium_url_Valid() const;

    qint32 getOrderNumber() const;
    void setOrderNumber(const qint32 &order_number);
    bool is_order_number_Set() const;
    bool is_order_number_Valid() const;

    QString getSmallHdUrl() const;
    void setSmallHdUrl(const QString &small_hd_url);
    bool is_small_hd_url_Set() const;
    bool is_small_hd_url_Valid() const;

    QString getSmallUrl() const;
    void setSmallUrl(const QString &small_url);
    bool is_small_url_Set() const;
    bool is_small_url_Valid() const;

    QString getThumbnailHdUrl() const;
    void setThumbnailHdUrl(const QString &thumbnail_hd_url);
    bool is_thumbnail_hd_url_Set() const;
    bool is_thumbnail_hd_url_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_large_hd_url;
    bool m_large_hd_url_isSet;
    bool m_large_hd_url_isValid;

    QString m_large_url;
    bool m_large_url_isSet;
    bool m_large_url_isValid;

    QString m_medium_hd_url;
    bool m_medium_hd_url_isSet;
    bool m_medium_hd_url_isValid;

    QString m_medium_url;
    bool m_medium_url_isSet;
    bool m_medium_url_isValid;

    qint32 m_order_number;
    bool m_order_number_isSet;
    bool m_order_number_isValid;

    QString m_small_hd_url;
    bool m_small_hd_url_isSet;
    bool m_small_hd_url_isValid;

    QString m_small_url;
    bool m_small_url_isSet;
    bool m_small_url_isValid;

    QString m_thumbnail_hd_url;
    bool m_thumbnail_hd_url_isSet;
    bool m_thumbnail_hd_url_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArticle_Image)

#endif // OAIArticle_Image_H
