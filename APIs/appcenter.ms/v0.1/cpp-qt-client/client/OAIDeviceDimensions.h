/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDeviceDimensions.h
 *
 * Physical device dimensions
 */

#ifndef OAIDeviceDimensions_H
#define OAIDeviceDimensions_H

#include <QJsonObject>

#include "OAIObject.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDeviceDimensions : public OAIObject {
public:
    OAIDeviceDimensions();
    OAIDeviceDimensions(QString json);
    ~OAIDeviceDimensions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getDepth() const;
    void setDepth(const OAIObject &depth);
    bool is_depth_Set() const;
    bool is_depth_Valid() const;

    OAIObject getHeight() const;
    void setHeight(const OAIObject &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    OAIObject getWidth() const;
    void setWidth(const OAIObject &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_depth;
    bool m_depth_isSet;
    bool m_depth_isValid;

    OAIObject m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    OAIObject m_width;
    bool m_width_isSet;
    bool m_width_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeviceDimensions)

#endif // OAIDeviceDimensions_H
