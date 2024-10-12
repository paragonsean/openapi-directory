/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIColor.h
 *
 * Base color for QR Code modules.
 */

#ifndef OAIColor_H
#define OAIColor_H

#include <QJsonObject>

#include "OAIGradient.h"
#include "OAIGradientStop.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGradientStop;

class OAIColor : public OAIObject {
public:
    OAIColor();
    OAIColor(QString json);
    ~OAIColor() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAngle() const;
    void setAngle(const qint32 &angle);
    bool is_angle_Set() const;
    bool is_angle_Valid() const;

    QList<OAIGradientStop> getStops() const;
    void setStops(const QList<OAIGradientStop> &stops);
    bool is_stops_Set() const;
    bool is_stops_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_angle;
    bool m_angle_isSet;
    bool m_angle_isValid;

    QList<OAIGradientStop> m_stops;
    bool m_stops_isSet;
    bool m_stops_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIColor)

#endif // OAIColor_H
