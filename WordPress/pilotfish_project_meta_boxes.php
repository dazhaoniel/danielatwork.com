<?php
/*
Plugin Name: Pilot Fish Project Custom Meta Boxes
Plugin URI: http://danielatwork.com/
Description: Create Meta Boxes for Pilot Fish Projects.
Version: 0.1
Author: Daniel Zhao
Author URI: http://danielatwork.com/
License: GPL v2 or higher
License URI: License URI: http://www.gnu.org/licenses/gpl-2.0.html
*/

if ( is_admin() ) {  //do nothing for front end requests
    add_action( 'load-post-new.php', 'pilotfish_project_meta_boxes_init' );
    add_action( 'load-post.php', 'pilotfish_project_meta_boxes_init' );
}

function pilotfish_project_meta_boxes_init() {
    new pilotfish_project_meta_boxes();
}
 
class pilotfish_project_meta_boxes {
    public function __construct() {
        add_action( 'add_meta_boxes', array( $this, 'add_meta_box' ) );
        add_action( 'save_post', array( $this, 'save' ) );
    }
 
    public function add_meta_box( $post_type ) {
        $post_types = array( 'project', 'pilotfish' );
        if ( in_array( $post_type, $post_types )) {
            add_meta_box(
                'pilotfish_box_id',            // Unique ID
                'Project Meta For Flask',      // Box title
                array( $this, 'render_form'), // Content callback
                $post_type
            );
        }
    }
 
    public function save( $post_id ) {
        if ( array_key_exists('pilotfish_project_url', $_POST ) ) {
            update_post_meta( $post_id,
               '_pilotfish_meta_value_project_url_key',
                $_POST['pilotfish_project_url']
            );
        }
        if ( array_key_exists('pilotfish_project_image_url', $_POST ) ) {
            update_post_meta( $post_id,
               '_pilotfish_meta_value_project_image_url_key',
                $_POST['pilotfish_project_image_url']
            );
        }
        if ( array_key_exists('pilotfish_project_year', $_POST ) ) {
            update_post_meta( $post_id,
               '_pilotfish_meta_value_project_year_key',
                $_POST['pilotfish_project_year']
            );
        }
    }
 
    public function render_form( $post ) {
    ?>
        <!-- Project URL -->
        <label for="pilotfish_project_url">Project URL</label>
        <?php $value = get_post_meta( $post->ID,
            '_pilotfish_meta_value_project_url_key', true ); ?>
        <p>
            <input type="text" name="pilotfish_project_url" id="pilotfish_project_url"
            class="postbox" value="<?php $value ? print $value : print '';
                ?>"/>
        </p>

        <!-- Project Image Url -->
        <label for="pilotfish_project_image_url">Project Image URL</label>
        <?php $value = get_post_meta( $post->ID,
            '_pilotfish_meta_value_project_image_url_key', true ); ?>
        <p>
            <input type="text" name="pilotfish_project_image_url" id="pilotfish_project_image_url"
            class="postbox" value="<?php $value ? print $value : print '';
                ?>"/>
        </p>

        <!-- Project Year -->
        <label for="pilotfish_project_year">Project Year</label>
        <?php $value = get_post_meta( $post->ID,
            '_pilotfish_meta_value_project_year_key', true ); ?>
        <p>
            <input type="text" name="pilotfish_project_year" id="pilotfish_project_year"
            class="postbox" value="<?php $value ? print $value : print '';
                ?>"/>
        </p>
    <?php
    }
}