'use strict';

/**
 * tyre service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::tyre.tyre');
