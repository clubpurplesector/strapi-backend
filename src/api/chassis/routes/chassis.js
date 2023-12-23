'use strict';

/**
 * chassis router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::chassis.chassis');
